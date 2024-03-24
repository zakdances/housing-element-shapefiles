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

from find_intersection_from_server import generate_request

load_dotenv(dotenv_path=Path('.env.local'))
PROJECT_ID = os.getenv('PROJECT_ID')
VIEWABLE_DATASETS = os.getenv('VIEWABLE_DATASETS')

client = bigquery.Client(project=PROJECT_ID)

def chunk_list(lst, chunk_size):
    chunked_list = [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
    return chunked_list

# def generate_shapefile(table_list, query_df):
def generate_shapefile(gdf, output_dir):
    dfs = []
    processed_docs = []
    none_found = []

    os.makedirs(output_dir, exist_ok=True)

    if len(gdf) > 0:
        # misc_dir = file_path / 'misc'
        # os.makedirs(output_dir, exist_ok=True)
        shapefile_dir_path = output_dir / "shapefile"
        gdf.to_file(shapefile_dir_path, driver='ESRI Shapefile')
        shutil.make_archive(shapefile_dir_path, 'zip', shapefile_dir_path)
        send2trash(shapefile_dir_path)
        print("shapefile created at " + str(output_dir.parent.stem))
    else:
        none_found.append(output_dir.stem)

        existing_shapefile_path = output_dir / "shapefile.zip"
        if existing_shapefile_path.exists():
            send2trash(existing_shapefile_path)
            print("invalid shapefile deleted")
        # if output_dir.is_dir() and not any(output_dir.iterdir()):
        #     send2trash(output_dir)
        #     print("empty output_dir deleted (" + str(output_dir) + ")")

        print("no intersection found")

    processed_docs.append(output_dir.stem)

    return


if __name__ == "__main__":
    generate_shapefile()


