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
            p.geometry AS geometry
        FROM
            `{PROJECT_ID}.{VIEWABLE_DATASETS}.*` AS s,
            UNNEST(s.table_rows) AS nested_rows
        JOIN
            `{PROJECT_ID}.parcels.all` AS p
        ON
            REGEXP_REPLACE(nested_rows.APN, r'[-_\s]', '') = REGEXP_REPLACE(p.APN, r'[-_\s]', '')
        WHERE
            REGEXP_CONTAINS(_TABLE_SUFFIX, r'^({joined_table_list})$')
    """
    query_job = client.query(query_3, job_config=job_config2)  # Make an API request.
    # query_df = query_job.to_dataframe()
    query_df = query_job.to_geodataframe(geography_column="geometry")
    return query_df

def generate_shapefile(table_list):
    # .replace("(", "⁀").replace(")", "‿")
    tables = list(map(lambda x: x["path"].stem, table_list))
    query_df = generate_request(tables)
    query_df['id'] = query_df['id'].replace("⁀", "(").replace("‿", ")")
    # query_df['geometryy'] = query_df['geometryy'].apply(lambda x: shape(x).__str__())
    # gdf = gpd.GeoDataFrame(query_df, geometry='geometry')
    # output_dir = output_dir_path / "temp"
    for table_obj in table_list:
        stem = table_obj["path"].stem
        # print(stem)
        output_path = table_obj["output"]
        filtered_gdf = query_df.query("id == @stem")
        if len(filtered_gdf) > 0:
            # print(filtered_gdf)
            print(stem)
            os.makedirs(output_path, exist_ok=True)
            shapefile_dir_path = output_path / "shapefile"
            filtered_gdf.to_file(shapefile_dir_path, driver='ESRI Shapefile')
            # Zip the shapefile directory
            shutil.make_archive(shapefile_dir_path, 'zip', shapefile_dir_path)
            send2trash(shapefile_dir_path)

    print("done!")
    # print(query_df)





