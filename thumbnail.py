import os
import glob
from time import sleep
import json
import jsonlines
import random
import pathlib
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
from google.cloud import storage
from PyPDF2 import PdfReader
import pymupdf as fitz
from send2trash import send2trash

dataset_id = "doc_metadata"
table_id = "all"

def generate_thumbnail(doc_path, project_id):

    # if isinstance(schema_filepath, str):
    #     with open(schema_filepath, 'r') as file:
    #         schema = json.load(file)


    doc_path = Path(doc_path)
    doc_filename = doc_path.name
    file_extension = doc_path.suffix.lstrip('.')
    filename_without_extension = doc_path.stem
    
    # print("resolve")
    # print(doc_path.resolve())
    reader = PdfReader(doc_path.resolve())
    page_count = len(reader.pages)

    new_image_path = None
    doc = fitz.open(doc_path.resolve())  # open document
    for i, page in enumerate(doc):
        zoom_x = 0.5  # horizontal zoom
        zoom_y = 0.5  # vertical zoom
        mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension
        pix = page.get_pixmap(matrix=mat)  # render page to an image
        new_image_filename = f"{filename_without_extension}_page_{i}.webp"
        new_image_path = pathlib.Path.cwd() / new_image_filename
        # print(new_image_path.name)
        pix.pil_save(new_image_path.name, optimize=True, zoom_x=0.5)

        break

    storage_client = storage.Client()
    bucket_name = "parcel_viewer_bucket"
    # Get a reference to the bucket you want to upload to
    bucket = storage_client.bucket(bucket_name)

    # Create a new blob object
    blob = bucket.blob(new_image_filename)

    try: 
        # Upload the file to the bucket
        blob.upload_from_filename("./" + new_image_path.name)
        send2trash(new_image_path.resolve())
        print("thumbnail success! (" + bucket_name + "/" + new_image_path.name + ")")
    except Exception as e:
        # Print an error message if the file could not be uploaded.
        print(e)

 
    # print(job.num_dml_affected_rows)
    
    return
