import os
import glob
from time import sleep
import json
import jsonlines
import random
import geopandas as gpd
import pandas as pd
import numpy as np
from pathlib import Path
from dotenv import load_dotenv
import apache_beam as beam
from apache_beam.io.gcp.internal.clients import bigquery
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.bigquery_tools import parse_table_schema_from_json
from google.cloud import bigquery
from google.cloud.exceptions import NotFound
from py_markdown_table.markdown_table import markdown_table

from src.find.find import find_tables_and_parcels
from update_doc_metadata import update_doc_metadata
from thumbnail import generate_thumbnail
from generate_shapefiles import generate_shapefile

load_dotenv(dotenv_path=Path('.env.local'))

HOUSING_ELEMENT_SCHEMA_FILEPATH = os.getenv('HOUSING_ELEMENT_SCHEMA_FILEPATH')
COUNTIES_DIR_PATH = os.getenv('COUNTIES_DIR_PATH')

PROJECT_ID = os.getenv('PROJECT_ID')
VIEWABLE_DATASETS = os.getenv('VIEWABLE_DATASETS')
MAIN_FILE_PATH = os.getenv('MAIN_FILE_PATH')

TEST_OUTPUT_DIR_PATH_sacramento_6th_draft040821 = os.getenv('TEST_OUTPUT_DIR_PATH_sacramento_6th_draft040821')
TEST_OUTPUT_DIR_PATH_sacramento_6th_adopted082021 = os.getenv('TEST_OUTPUT_DIR_PATH_sacramento_6th_adopted082021')
TEST_OUTPUT_DIR_PATH_sacramento_6th_adopted121421 = os.getenv('TEST_OUTPUT_DIR_PATH_sacramento_6th_adopted121421')
TEST_OUTPUT_DIR_PATH_mill_valley_6th_draft082322 = os.getenv('TEST_OUTPUT_DIR_PATH_mill_valley_6th_draft082322')

def chunk_list(lst, chunk_size):
    chunked_list = [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
    return chunked_list

def list_tables(project_id):
    client = bigquery.Client(project=project_id)

    dataset_ref = client.dataset(VIEWABLE_DATASETS)
    tables = client.list_tables(dataset_ref)
    return list(tables)

def convert_apn_values_to_strings(json_obj):
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            if key == "APN":
                json_obj[key] = str(value)
            elif isinstance(value, (dict, list)):
                convert_apn_values_to_strings(value)
    elif isinstance(json_obj, list):
        for item in json_obj:
            convert_apn_values_to_strings(item)

def beam_to_DB(data, db_table, schema):

    if isinstance(schema, str):
        with open(schema, 'r') as file:
            schema = json.load(file)
    
    # if not isinstance(data, list):
    #     data = [data]

    # Create a pipeline.
    pipeline = beam.Pipeline()
    pcollection = pipeline | beam.Create(data)

    # Write data to BigQuery.
    pcollection | beam.io.WriteToBigQuery(
        db_table,
        schema={"fields": schema},
        method='BATCH_INSERT',
        write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE,
        create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED)

    # Run the pipeline.
    pipeline.run().wait_until_finish()

def bq_client_to_db(data, db_table, schema):

    # Load the schema from the local JSON file
    if isinstance(schema, str):
        with open(schema, 'r') as file:
            schema = json.load(file)

    # if not isinstance(data, list):
    #     data = [data]
    
    # print(data)

    my_split = db_table.split(":")
    # Specify your BigQuery project ID and dataset ID
    project_id = my_split[0]
    dataset_id = my_split[1].split(".")[0]
    table_id = my_split[1].split(".")[1].replace("(", "⁀").replace(")", "‿")

     # Create a BigQuery client
    client = bigquery.Client(project=project_id)

    # Define the BigQuery dataset and table
    # dataset_ref = client.dataset(dataset_id)
    # table_ref = dataset_ref.table(table_id)
    
    # Try to get the table.
    try:
        print("starting")


            
        # table = pd.DataFrame(data)

        # Update the "tables" column with the modified data
        table_json = json.loads(data.to_json(orient='records'))
        # print("outgoing json data: ")
        # print(table_json)
        job_config = bigquery.LoadJobConfig(schema=schema, write_disposition='WRITE_TRUNCATE')
        job = client.load_table_from_json(table_json, dataset_id + '.' + table_id, job_config=job_config)
        result = job.result()


        # Check the query job status
        if job.state == 'DONE':
            print('Upsert completed successfully.')
            print(result)

            # Get the number of inserted and updated rows
            inserted_rows = job.output_rows
            # updated_rows = job.num_dml_affected_rows

            # Print the results
            print(f"{inserted_rows} records were inserted.")
            # print(f"{updated_rows} records were updated.")

        else:
            print('Upsert job failed.')
        
        # Check for errors
        if job.errors:
            for error in job.errors:
                print(f"Error: {error['message']}")
        else:
            print("Data loaded successfully")


    except NotFound:
        # The table does not exist, so create it.
        # table = bigquery.Table(table_ref, schema=schema)
        # client.create_table(
        #     table
        # )
        print("table not created yet, sleeping for 5 seconds until done.")
        sleep(5)
        print("Done")
        # table = client.get_table(table_ref)
    except Exception as e:
        error_message = str(e)  # Convert the exception object to a string
        print("Oh no. An error occurred:", error_message)

    return

def create_filtered_json(file_name, apn_rows):
    rows = []
    
    for row in apn_rows:
        page_number = row[1]
        if not isinstance(page_number, int):
            page_number = int(page_number)
            # print(type(page_number))
            # raise TypeError("Variable is not an integer.")
        rows.append({
            "APN": str(row[0]),
            "page_number": page_number,
        })
    return {
        "table_name": file_name,
        "table_rows": rows
    }

def main():


    # county = "Sacramento"
    # city = "Sacramento"
    # doc_name = "sacramento-6th-draft040821.pdf"
    # doc_name_no_extension = os.path.splitext(doc_name)[0]

    # city_directory = os.path.join(counties_path_name, county, "cities", city)
    # city_output_directory = os.path.join(city_directory, "output")
    # doc_output_directory = os.path.join(city_output_directory, doc_name_no_extension)
    # doc_input_filepath = os.path.join(city_directory, "input", doc_name)

    with open(MAIN_FILE_PATH, 'r') as file:
        main_data = json.load(file)

    SCAG = []
    ABAG = []
    SACOG = []
    SANDAG = []

    for city in main_data:
        if city["planning_agency"] == "SACOG":
            SACOG.append(city['city'])
        elif city["planning_agency"] == "ABAG":
            ABAG.append(city['city'])
        elif city["planning_agency"] == "SCAG":
            SCAG.append(city['city'])
        
    print(SACOG)
    # orgs_to_process = (ABAG + SACOG + SCAG)
    orgs_to_process = SACOG


    my_apn_datasets = list(map(lambda x: x.table_id, list_tables(PROJECT_ID)))
    my_apn_datasets = list(map(lambda x: x.replace("⁀", "(").replace("‿", ")"), my_apn_datasets))
    
    # print(my_apn_datasets)
    all_docs = []
    
    for county_dir in os.scandir(COUNTIES_DIR_PATH):
        if county_dir.is_dir():
            # if county_dir.name != "Orange":
            #     print("orange")
            #     continue
            _cities_dir = list(os.scandir(os.path.join(county_dir.path, "cities")))
            cities_dirs = list(filter(lambda x: x.is_dir(), _cities_dir))

            for file_2 in cities_dirs:
                # if file_2.is_dir():
                
                if file_2.name in orgs_to_process:
                    # print(file_2.name)
                    output_paths = os.path.join(file_2.path, "output")

                    if os.path.exists(output_paths):
                        for entry in os.scandir(output_paths):
                            
                            if entry.is_dir():

                                # print(entry.name)
                                all_docs.append(entry.path)
                                # print(entry.path)
                    # else:
                    #     print("no input: ")
                    #     print(input_paths)
                    #     print("___________ no input: ")

            

    
    # city_filtered_output_directory = os.path.join(city_directory, "filtered output")
    # contents = os.listdir(city_output_directory)
    accumulator = {}

    for path_to_execute_on in sorted(all_docs, key=lambda x: Path(x).name.lower()):
        
        # path_to_execute_on = Path(TEST_OUTPUT_DIR_PATH_sacramento_6th_draft040821 + "/aws")
        # path_to_execute_on = Path(TEST_OUTPUT_DIR_PATH_sacramento_6th_adopted082021 + "/aws")
        # path_to_execute_on = Path(TEST_OUTPUT_DIR_PATH_mill_valley_6th_draft082322 + "/aws")

        # print(Path(path_to_execute_on).name)
        path_to_execute_on = Path(path_to_execute_on)
        city_name = path_to_execute_on.parent.parent.stem
        aws_path = path_to_execute_on / "aws"
        camelot_path = path_to_execute_on / "camelot"
        chosen_path = None
        if aws_path.exists():
            chosen_path = aws_path
        elif camelot_path.exists():
            chosen_path = camelot_path
        else:
            raise Exception("No output found for " + path_to_execute_on.parents[2])
        if not city_name in accumulator:
            accumulator[city_name] = {"documents": 0, "tables": 0, "apns": 0, "org": "SACOG"}
        accumulator[city_name]["documents"] += 1
        

        
        input_path = path_to_execute_on.parents[1] / "input" / (path_to_execute_on.stem + ".pdf")
        # print(input_path)
        # print(str(os.path.exists(input_path)))
        print("----------------------")
        print(city_name)
        print(path_to_execute_on.stem)
        # print("----------------------")

        # if path_to_execute_on.stem in my_apn_datasets:
        #     print("already exists. Skipping...")
        #     continue


        df = find_tables_and_parcels(chosen_path)
        df.to_json('temp/output.json', orient='records')
        accumulator[city_name]["tables"] += len(df)
        count_of_apns = df['table_rows'].apply(lambda x: len(x)).sum()
        accumulator[city_name]["apns"] += count_of_apns

        # if len(df) > 0:
        #     target = PROJECT_ID + ":viewable_datasets." + path_to_execute_on.stem
        #     bq_client_to_db(df, target, HOUSING_ELEMENT_SCHEMA_FILEPATH)
        #     update_doc_metadata(input_path, PROJECT_ID)
        #     generate_thumbnail(input_path, PROJECT_ID)
  
    paths_that_need_shapefiles = list(map(lambda x: {"path": Path(x), "output": Path(x) / "misc"}, all_docs))
    paths_that_need_shapefiles = list(filter(lambda x: x["path"].stem in my_apn_datasets, paths_that_need_shapefiles))
    
    for chunk in chunk_list(paths_that_need_shapefiles, 50):
        # for path_obj in chunk:
        #     print(path_obj)
            # print("path_to_execute_on")
            # print(path_obj["path"])
            # print(path_obj["output"])

        # generate_shapefile(chunk)
        print('done')


    print(accumulator)
    data_for_markdown = []
    for key, value in accumulator.items():
        data_for_markdown.append({
            "city": key,
            "documents": value["documents"],
            "tables": value["tables"],
            "apns": value["apns"]
        })
    markdown = markdown_table(data_for_markdown).get_markdown()
    print(markdown)
    return

if __name__ == '__main__':
    main()

