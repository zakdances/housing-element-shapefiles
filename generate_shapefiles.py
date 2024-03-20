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

    if len(gdf) > 0:
        # misc_dir = file_path / 'misc'
        os.makedirs(output_dir, exist_ok=True)
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
        if output_dir.is_dir() and not any(output_dir.iterdir()):
            send2trash(output_dir)
            print("empty output_dir deleted (" + str(output_dir) + ")")

        print("no intersection found")

    processed_docs.append(output_dir.stem)

    return

    # Specify a pattern with multiple asterisks
    pattern = 'counties/*/cities/*/output/*'

    # Use glob to find files that match the pattern
    file_list = glob.glob(pattern)

    paths = []
    # Loop through the list of matching files
    for file_path in file_list:
        # print(f"File: {file_path}")
        paths.append(Path(file_path).resolve())

    for file_paths in chunk_list(paths, 1):
        for file_path in file_paths:
            print(f"File: {file_path.stem}")
            

        stems = list(map(lambda x: x.stem, file_paths))
        server_intersection_df = generate_request(stems)
        dfs.append(server_intersection_df)

        for file_path in file_paths:
            filtered_gdf = server_intersection_df[server_intersection_df['id'] == file_path.stem]
            # print(filtered_gdf)

            if len(filtered_gdf) > 0:
                misc_dir = file_path / 'misc'
                os.makedirs(misc_dir, exist_ok=True)
                shapefile_dir_path = misc_dir / "shapefile"
                filtered_gdf.to_file(shapefile_dir_path, driver='ESRI Shapefile')
                shutil.make_archive(shapefile_dir_path, 'zip', shapefile_dir_path)
                send2trash(shapefile_dir_path)
                print("shapefile created at " + str(misc_dir.parent.stem))
            else:
                none_found.append(file_path.stem)
                print("no intersection found")

            processed_docs.append(file_path.stem)
    
    # merged_gdf = gpd.concat(dfs, ignore_index=True)
    # print(merged_gdf)
    print("done!")
    print("none found: ")
    print(none_found)
        
    return 
    # .replace("(", "⁀").replace(")", "‿")
    # tables = list(map(lambda x: x["path"].stem, table_list))
    # query_df = generate_request(tables)
    
    # query_df['id'] = query_df['id'].replace("⁀", "(").replace("‿", ")")
    # query_df['geometryy'] = query_df['geometryy'].apply(lambda x: shape(x).__str__())
    # gdf = gpd.GeoDataFrame(query_df, geometry='geometry')
    # output_dir = output_dir_path / "temp"
    for table_obj in table_list:
        stem = table_obj.stem
        # print(stem)
        output_path = table_obj / "output"
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


if __name__ == "__main__":
    generate_shapefile()


