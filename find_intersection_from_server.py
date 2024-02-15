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

def perform_query(joined_table_list, job_config, limit, offset):
    joined_table_list = list(map(lambda x: x.replace("(", "⁀").replace(")", "‿"), joined_table_list))
    joined_table_list_string = "|".join(joined_table_list)
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
            `{PROJECT_ID}.parcels.all` AS p
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
        
        LIMIT {limit}
        OFFSET {offset}
    """
    print("starting intersection query at offset " + str(offset) + " for " + joined_table_list_string)
    query_job = client.query(query_3, job_config=job_config)  # Make an API request.
    print("done executing query!")
    return query_job

def generate_request(table_list):
    # table_list = list(map(lambda x: x.replace("(", "⁀").replace(")", "‿"), table_list))
    
    dfs = []

    for table_list in list(chunked(table_list, 20)):
        # joined_table_list = table_name
    
        batch_size = 3000
        offset = 0

        while True:
            job_config2 = bigquery.QueryJobConfig()
            query_job = perform_query(table_list, job_config2, batch_size, offset)
            print("gettings result...")
            results = query_job.result()
            print("done getting result!")

            if results.total_rows > 0:
                dfs.append({'table_name': str(table_list), 'query_job': query_job})
            
            # Increment the offset for the next iteration
            offset += batch_size

            # Stop the loop if the last batch had fewer than batch_size rows
            if results.total_rows < batch_size:
                break 
            

    print("converting query data to geopandas dataframe...")
    dfs = list(map(convert_to_geopandas_dataframe, dfs))

    print("done 1!")
    merged_gdf = pd.concat(dfs, ignore_index=True)
    print("done 2!")
    merged_gdf['id'] = merged_gdf['id'].replace("⁀", "(").replace("‿", ")")
    print("done 3!")
    return merged_gdf