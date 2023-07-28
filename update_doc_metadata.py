import os
import glob
from time import sleep
import json
import jsonlines
import random
from pathlib import Path
import geopandas as gpd
import pandas as pd
import numpy as np
import apache_beam as beam
from apache_beam.io.gcp.internal.clients import bigquery
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.bigquery_tools import parse_table_schema_from_json
from google.cloud import bigquery
from google.cloud.exceptions import NotFound
from pypdf import PdfReader
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path('.env.local'))

HOUSING_ELEMENT_METADATA_SCHEMA_FILEPATH = os.getenv('HOUSING_ELEMENT_METADATA_SCHEMA_FILEPATH')
MAIN_FILE_PATH = os.getenv('MAIN_FILE_PATH')

dataset_id = "doc_metadata"
table_id = "all"

def update_doc_metadata(doc_path, project_id):

    if isinstance(HOUSING_ELEMENT_METADATA_SCHEMA_FILEPATH, str):
        with open(HOUSING_ELEMENT_METADATA_SCHEMA_FILEPATH, 'r') as file:
            schema = json.load(file)
    
    with open(MAIN_FILE_PATH, 'r') as file:
        main_data = json.load(file)

    # my_split = db_table.split(":")
    # Specify your BigQuery project ID and dataset ID
    # project_id = my_split[0]
    

    doc_path = Path(doc_path)
    doc_filename = doc_path.name
    file_extension = doc_path.suffix.lstrip('.')
    filename_without_extension = doc_path.stem
    
    # print("resolve")
    # print(doc_path.resolve())
    reader = PdfReader(doc_path.resolve())
    page_count = len(reader.pages)

    new_data = {
        "doc_name": filename_without_extension, 
        "page_count": page_count, 
        "file_type": file_extension,
        "download_link": None,
    }

    matched_link = None
    # Get city and download link
    for city in main_data:
        housing_element_link_list = city["housing_element"]
        city_name = city["city"]
        for link in housing_element_link_list:
            # print("link")
            # link = link.replace('(', '⁀').replace(')', '‿')
            # print(link)
            # print(doc_filename)
            if doc_filename in link:
                matched_link = link
                break
        if matched_link:
            break
    
    if not matched_link:
        raise ValueError("No matched link found for " + doc_filename)
    
    new_data["download_link"] = matched_link



     # Create a BigQuery client
    client = bigquery.Client(project=project_id)
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    # table = client.get_table(table_ref)
    df = client.list_rows(table_ref).to_dataframe()
    df = df.drop(df[df['doc_name'] == filename_without_extension].index)

    new_data_series = pd.Series(new_data)
    # print(pd.DataFrame(new_data_series))
    df = pd.concat([df, new_data_series.to_frame().T], ignore_index=True)

    print(str(len(df)))

    table_json = json.loads(df.to_json(orient='records'))

    job_config = bigquery.LoadJobConfig(schema=schema, write_disposition='WRITE_TRUNCATE')
    job = client.load_table_from_json(table_json, table_ref, job_config=job_config)
    result = job.result()

    # print(job.num_dml_affected_rows)
    print("metadata success!")
    return
