import os
import glob
import shutil
from time import sleep
import json
import jsonlines
import random
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

PROJECT_ID = os.getenv('PROJECT_ID')
VIEWABLE_DATASETS = os.getenv('VIEWABLE_DATASETS')

client = bigquery.Client(project=PROJECT_ID)

def generate_request(table_list):
    table_list = list(map(lambda x: x.replace("(", "⁀").replace(")", "‿"), table_list))
    joined_table_list = "|".join(table_list)
    job_config2 = bigquery.QueryJobConfig()
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
            REGEXP_CONTAINS(_TABLE_SUFFIX, r'^({joined_table_list})$')
        AND
            m.county = p.county
    """
    query_job = client.query(query_3, job_config=job_config2)  # Make an API request.
    # query_df = query_job.to_dataframe()
    query_df = query_job.to_geodataframe(geography_column="geometry")
    query_df['id'] = query_df['id'].replace("⁀", "(").replace("‿", ")")
    return query_df