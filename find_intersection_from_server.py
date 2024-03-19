import os
import glob
import shutil
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

load_dotenv(dotenv_path=Path('.env.local'))
PROJECT_ID = os.getenv('PROJECT_ID')
VIEWABLE_DATASETS = os.getenv('VIEWABLE_DATASETS')

client = bigquery.Client(project=PROJECT_ID)

def convert_to_geopandas_dataframe(query_job_obj):
    query_job = query_job_obj['query_job']
    print("Converting data of " + query_job_obj['table_name'] + " to geodataframe...")
    query_df = query_job.to_geodataframe(geography_column="geometry")
    print("done!")
    return query_df

def perform_query_v2(job_config, incoming_apns, parcel_table_name = 'all'):
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
            REGEXP_REPLACE(LOWER(p.APN), '[-_]', '') = REGEXP_REPLACE(LOWER(incoming_apn), '[-_]', '')

    """
    print("starting intersection query for " + "joined_table_list_string")
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

def generate_request(incoming_df_container):
    # table_list = list(map(lambda x: x.replace("(", "⁀").replace(")", "‿"), table_list))
    
    # dfs = []
    incoming_df = incoming_df_container["df"]
    county = incoming_df["county_name"]
    newGdf = gpd.GeoDataFrame(columns=['geometry'], geometry='geometry')

    # for table_list in list(chunked(table_list, 20)):
    for index, row in incoming_df.iterrows():
        # joined_table_list = table_name
        table_name = str(row["table_name"])
        parcels = list(row["table_rows"])
        table_order = str(row["table_order"])
        
        for parcels_chunk in list(chunked(parcels, 2000)):

            apns_chunk = list(map(lambda x: x["APN"], parcels_chunk))
            # print(parcels_chunk)
            # batch_size = 3000
            # offset = 0

            # while True:
            job_config2 = bigquery.QueryJobConfig()
            query_job = perform_query_v2(job_config2, apns_chunk, county)

            print("gettings result...")
            results = query_job.result()
            total_rows = results.total_rows
            print("done getting result!")
            print(total_rows)
            # print(list(results))

            
            # if total_rows > 0:
            gdf = query_job.to_geodataframe(geography_column="geometry")
            gdf['table_order'] = table_order
            # print(gdf)
            newGdf = newGdf.append(gdf, ignore_index=True)
            
            # if not isinstance(newGdf, gpd.GeoDataFrame):
            #     newGdf = gdf
            #     print("buh")
            # else:
            #     print("guh 1")
            #     print(newGdf)
            #     newGdf = newGdf.merge(gdf, on='table_order')
            #     print("guh 2")
            #     print(newGdf)

            print("new chunk processed")
            print(newGdf)
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
    print(newGdf)
    print("done 1!")
    # merged_gdf = pd.concat(dfs, ignore_index=True)
    # print("done 2!")
    # merged_gdf['id'] = merged_gdf['id'].replace("⁀", "(").replace("‿", ")")
    # print("done 3!")
    return newGdf