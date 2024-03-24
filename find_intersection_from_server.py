import os
import glob
import shutil
import asyncio
import re
from time import sleep
import json
import jsonlines
import random
from more_itertools import chunked
import geopandas as gpd
import pandas as pd
import numpy as np
import shapefile
from shapely.geometry import shape
from pathlib import Path
from dotenv import load_dotenv
import apache_beam as beam
from apache_beam.io.gcp.internal.clients import bigquery
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.bigquery_tools import parse_table_schema_from_json
from google.cloud import bigquery
from google.cloud.exceptions import NotFound
from send2trash import send2trash

# REGEXP_REPLACE(nested_rows.APN, r'[-_\s]', '') = REGEXP_REPLACE(p.APN, r'[-_\s]', '')
# REGEXP_REPLACE(p.APN, r'[-_\s]', '') LIKE CONCAT('%', REGEXP_REPLACE(nested_rows.APN, r'[-_\s]', ''), '%')
# p.APN LIKE CONCAT('%', nested_rows.APN, '%')
"""The purpose of these functions is to pair the APNs from the excel files to their respective geometry.

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""

load_dotenv(dotenv_path=Path('.env.local'))
PROJECT_ID = os.getenv('PROJECT_ID')
VIEWABLE_DATASETS = os.getenv('VIEWABLE_DATASETS')
CACHE_DIR = Path(os.getenv('CACHE_DIR'))

client = bigquery.Client(project=PROJECT_ID)

def convert_to_geopandas_dataframe(query_job_obj):
    query_job = query_job_obj['query_job']
    print("Converting data of " + query_job_obj['table_name'] + " to geodataframe...")
    query_df = query_job.to_geodataframe(geography_column="geometry")
    print("done!")
    return query_df

def perform_query_v2(job_config, incoming_apns, county, parcel_table_name = 'all'):
    # print(incoming_apns)
    query_3 = f"""
        SELECT
            p.APN as apn,
            p.county as county,
            -- p.state,
            -- p.country
            p.geometry AS geometry
        FROM
            `{PROJECT_ID}.parcels.{parcel_table_name}` AS p
        JOIN 
            UNNEST(@incoming_apns) AS incoming_apn
        ON
            RTRIM( REGEXP_REPLACE(LOWER(p.APN), '[^a-zA-Z0-9]', ''), '0') = RTRIM( REGEXP_REPLACE(LOWER(incoming_apn), '[^a-zA-Z0-9]', ''), '0')
            AND
            LOWER(p.county) = LOWER('{county}')

    """
    print("starting intersection query for " + str(len(incoming_apns)))
    print("at " + f"""{PROJECT_ID}.parcels.{parcel_table_name}""")

    # Set up query parameters
    query_params = [
        bigquery.ArrayQueryParameter("incoming_apns", "STRING", incoming_apns)
    ]

    query_job = client.query(
        query_3, 
        job_config=bigquery.QueryJobConfig(
            query_parameters=query_params
        )
    )  # Make an API request.
    print("done setting up query!")
    return query_job

def perform_query(joined_table_list, job_config, parcel_table_name):
    joined_table_list = list(map(lambda x: x.replace("(", "⁀").replace(")", "‿"), joined_table_list))
    joined_table_list_string = "|".join(joined_table_list)

    if not parcel_table_name:
        parcel_table_name = 'all'

    query_3 = f"""
        SELECT
            _TABLE_SUFFIX AS id,
            s.table_name,
            s.table_order,
            nested_rows.APN,
            nested_rows.page_number,
            nested_rows.row_number,
            p.APN AS server_apn,
            p.county AS server_county,
            m.county AS meta_county,
            p.geometry AS geometry
        FROM
            `{PROJECT_ID}.{VIEWABLE_DATASETS}.*` AS s,
            UNNEST(s.table_rows) AS nested_rows
        JOIN
            `{PROJECT_ID}.parcels.{parcel_table_name}` AS p
        ON
            REGEXP_REPLACE(p.APN, r'[-_\s]', '') LIKE CONCAT('%', REGEXP_REPLACE(nested_rows.APN, r'[-_\s]', ''), '%')

        JOIN
            `{PROJECT_ID}.doc_metadata.all` AS m
        ON
            m.doc_name = _TABLE_SUFFIX

        WHERE
            REGEXP_CONTAINS(_TABLE_SUFFIX, r'^({joined_table_list_string})$')
        AND
            m.county = p.county
        
        LIMIT 5
    """
    print("starting intersection query for " + joined_table_list_string)
    print("at " + f"""{PROJECT_ID}.parcels.{parcel_table_name}""")
    query_job = client.query(query_3, job_config=job_config)  # Make an API request.
    print("done executing query!")
    return query_job

async def generate_request(incoming_df_container):
    # await asyncio.sleep(0.25)
    # table_list = list(map(lambda x: x.replace("(", "⁀").replace(")", "‿"), table_list))
    
    # dfs = []
    incoming_df = incoming_df_container.df
    county = incoming_df_container.county_name
    cache_destination = CACHE_DIR / incoming_df_container.agency_name / "counties" / incoming_df_container.county_name / "cities" / incoming_df_container.city_name / (incoming_df_container.doc_file_name() + ".geojson")
    newGdf = gpd.GeoDataFrame(columns=['apn', 'geometry'], geometry='geometry')
    parcel_apns_debug = []
    
    for i, row in incoming_df.iterrows():
        for minirow in list(row["table_rows"]):
            print(minirow)

    raise Exception("done!")

    if cache_destination.exists():
        print("getting intersection geodataframe from cache...")
        newGdf = pd.concat([newGdf, gpd.read_file(cache_destination)], ignore_index=True)
        
        for index, row in incoming_df.iterrows():
            parcels = list(row["table_rows"])
            parcel_apns_debug.extend( list( map(lambda x: x['APN'], parcels) ) )

        debug_print(newGdf, parcel_apns_debug)
        return newGdf

    print("Starting server query for " + incoming_df_container.doc_file_name())
    # for table_list in list(chunked(table_list, 20)):
    for index, row in incoming_df.iterrows():
        # joined_table_list = table_name
        # table_name = str(row["table_name"])
        parcels = list(row["table_rows"])
        parcel_apns_debug.extend( list( map(lambda x: x['APN'], parcels) ) )
        table_order = str(row["table_order"])
        
        for parcels_chunk in list(chunked(parcels, 2000)):

            apns_chunk = list(map(lambda x: x["APN"], parcels_chunk))
            # print(parcels_chunk)
            # batch_size = 3000
            # offset = 0

            # while True:
            job_config2 = bigquery.QueryJobConfig()
            query_job = perform_query_v2(job_config2, apns_chunk, county, 'all_clustered_by_county')

            print("gettings result...")
            # results = query_job.result()
            # total_rows = results.total_rows
            
            # print(list(results))

            
            # if total_rows > 0:
            gdf = query_job.to_geodataframe(geography_column="geometry")
            gdf['table_order'] = table_order
            print("done getting result!")
            print("total rows: " + str(len(gdf)))
            # print(gdf)
            newGdf = pd.concat([newGdf, gdf], ignore_index=True)
            
            if not isinstance(newGdf, gpd.GeoDataFrame):
                raise Exception("not a geodataframe!")
            # else:
            #     print("guh 1")
            #     print(newGdf)
            #     newGdf = newGdf.merge(gdf, on='table_order')
            #     print("guh 2")
            #     print(newGdf)

            print("new chunk processed")
            # print(newGdf)
        
        # dfs.append({'table_name': table_name, 'table': newGdf, 'table_order': table_order})
            
        # Increment the offset for the next iteration
        # offset += batch_size

        # Stop the loop if the last batch had fewer than batch_size rows
        # if results.total_rows < batch_size:
        #     break 
    # if newGdf.empty:
    #     raise Exception("newGdf is empty")

    print("converting query data to geopandas dataframe...")
    # newGdf = newGdf.set_geometry("geometry")
    # print(newGdf)
    print("done 1!")
    
    # column_values_debug = newGdf['apn'].tolist()
    # non_intersecting = find_non_shared_strings(parcel_apns_debug, column_values_debug)
    # print(non_intersecting)
    # print(str(len(non_intersecting)) + " out of " + str(len(column_values_debug)))

    # merged_gdf = pd.concat(dfs, ignore_index=True)
    # print("done 2!")
    # merged_gdf['id'] = merged_gdf['id'].replace("⁀", "(").replace("‿", ")")
    # print("done 3!")
    print('done! now writing json to cache')
    # Write to a temp file for debugging

    os.makedirs(cache_destination.parent, exist_ok=True)
    with open(cache_destination, 'w') as f:
        f.write(newGdf.to_json())

    print(incoming_df_container.doc_file_name())
    debug_print(newGdf, parcel_apns_debug)

    return newGdf

def debug_print(newGdf, parcel_apns_debug):
    column_values_debug = newGdf['apn'].tolist()
    non_intersecting = find_non_shared_strings(parcel_apns_debug, column_values_debug)
    print(non_intersecting)
    print(str(len(non_intersecting)) + " out of " + str(len(parcel_apns_debug)) + " have no match.")

def remove_hyphens_and_underscores(s):
    s = s.lower()
    s = s.rstrip('0')
    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    return s

def find_non_shared_strings(list1, list2):
    list2 = list( map(lambda x: remove_hyphens_and_underscores(x), list2) )
    non_shared = list( filter(lambda x: remove_hyphens_and_underscores(x) not in list2, list1) )
    
    # set1 = {remove_hyphens_and_underscores(s) for s in list1}
    # set2 = {remove_hyphens_and_underscores(s) for s in list2}
    # non_shared = set1.symmetric_difference(set2)
    return non_shared