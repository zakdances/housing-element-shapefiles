# This is the main file for this repo.

import os
import glob
import sys
import argparse
from time import sleep
from collections import OrderedDict
import json
# import jsonlines
import asyncio
from itertools import groupby
from more_itertools import bucket, unique_everseen, chunked
import random
import geopandas as gpd
import pandas as pd
import numpy as np
from pathlib import Path
from dotenv import load_dotenv

from src.util.data_path import data_path
# import apache_beam as beam
# from apache_beam.io.gcp.internal.clients import bigquery
# from apache_beam.options.pipeline_options import PipelineOptions
# from apache_beam.io.gcp.bigquery_tools import parse_table_schema_from_json
from google.cloud import bigquery
from google.cloud.exceptions import NotFound
# from py_markdown_table.markdown_table import markdown_table
from pytablewriter import MarkdownTableWriter

from src.find.find import find_tables_and_parcels
from src.find_v2.find import find_tables_and_parcels_v2
from src.util.df_container import Df_Container
from update_doc_metadata import update_doc_metadata
from thumbnail import generate_thumbnail
from generate_shapefiles import generate_shapefile
from find_intersection_from_server import generate_request

load_dotenv(dotenv_path=Path('.env.local'))

# Load environment variables
HOUSING_ELEMENT_SCHEMA_FILEPATH = os.getenv('HOUSING_ELEMENT_SCHEMA_FILEPATH')
COUNTIES_DIR_PATH = os.getenv('COUNTIES_DIR_PATH')
PROJECT_ID = os.getenv('PROJECT_ID')
VIEWABLE_DATASETS = os.getenv('VIEWABLE_DATASETS')
MAIN_FILE_PATH = os.getenv('MAIN_FILE_PATH')

TEST_OUTPUT_DIR_PATH_sacramento_6th_draft040821 = os.getenv('TEST_OUTPUT_DIR_PATH_sacramento_6th_draft040821')
TEST_OUTPUT_DIR_PATH_sacramento_6th_adopted082021 = os.getenv('TEST_OUTPUT_DIR_PATH_sacramento_6th_adopted082021')
TEST_OUTPUT_DIR_PATH_sacramento_6th_adopted121421 = os.getenv('TEST_OUTPUT_DIR_PATH_sacramento_6th_adopted121421')
TEST_OUTPUT_DIR_PATH_mill_valley_6th_draft082322 = os.getenv('TEST_OUTPUT_DIR_PATH_mill_valley_6th_draft082322')

# with open(MAIN_FILE_PATH, 'r') as file:
#     main_data = json.load(file)

def hasXlsxFiles(path):
    path = Path(path)

    # Check if the path exists
    if not path.exists():
        return False

    # Check if the path is a directory
    if not path.is_dir():
        return False

    # Check if there are any .xlsx files in the directory
    for file in os.listdir(str(path)):
        if file.endswith('.xlsx'):
            return True

    return False

async def _execute_task(semaphore, task_function, args, current_task_number = None, max_task_number = None):
    async with semaphore:
        
        if current_task_number != None and max_task_number != None:
            print("task " + str(current_task_number) + " of " + str(max_task_number) + " started! ------------")
        else:
            print("task started! ------------")
        
        async_result = await task_function(*args)
        # await asyncio.sleep(1)
        print("task done!")
        return async_result

def get_agency_from_city_name(city_name):
    # with open(MAIN_FILE_PATH, 'r') as file:
    #     main_data = json.load(file)
    for city in main_data:
        # city_name = city['city']
        agency_name = city["planning_agency"]
        if city_name == city['city']:
            return agency_name


def delete_readme_tables():
    file_path = "./README.md"
    target_string = "## Results"
    # Open the file in read mode
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find the index of the line containing the target string
    line_index = next((i for i, line in enumerate(lines) if target_string in line), None)

    # If the target string is found, truncate the file up to that line
    if line_index is not None:
        with open(file_path, 'w') as file:
            file.writelines(lines[:line_index + 1])

def list_tables(project_id):
    client = bigquery.Client(project=project_id)

    dataset_ref = client.dataset(VIEWABLE_DATASETS)
    tables = client.list_tables(dataset_ref)
    return list(tables)

def list_doc_metadata(project_id):
    client = bigquery.Client(project=project_id)

    job_config2 = bigquery.QueryJobConfig()
    query_3 = f"""
        SELECT s.doc_name
        FROM
            `{project_id}.doc_metadata.all` AS s
        WHERE
            s.city IS NULL
    """
    query_job = client.query(query_3, job_config=job_config2)
    df = query_job.to_dataframe()
    return df

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
            "page_numberrr": page_number,
        })
    return {
        "table_name": file_name,
        "table_rows": rows
    }

def getPaths(orgs_to_process):
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
    return all_docs

async def main():

    parser = argparse.ArgumentParser()
    # parser.add_argument('--agency', type=str, help='which planning agency to process')
    parser.add_argument(
        '--pair', 
        nargs=3, 
        action='append', 
        metavar=('COUNTY', 'CITY', 'SOURCE'),
        help='Add a county-city-source pair. Can be used multiple times.'
    )

    # parser.add_argument('--city', type=str, help='which city to process')
    # parser.add_argument('--county', type=str, help='which county to process')
    parser.add_argument('--save', type=bool, help='save shape file and append meta data to readme')
    args = parser.parse_args()

    if not any(vars(args).values()):
        raise Exception("Please provide a county and a city to proceed.")
    # If agency is provied, city and county should not be provided
    if not args.pair or len(args.pair) == 0:
        raise Exception("Please provide at least one county and city pair to proceed.")
    
    # If agency is provided, it should be one of the following
    # if args.agency and args.agency not in ["SCAG", "ABAG", "SACOG"]:
    #     raise Exception("Not a valid agency name. Choose SCAG, ABAG, or SACOG.")


    

    # SCAG = []
    # ABAG = []
    # SACOG = []
    # SANDAG = []

    # for city in main_data:
    #     city_name = city['city']
    #     agency_name = city["planning_agency"]

    #     if agency_name == "SACOG":
    #         SACOG.append(city_name)
    #     elif agency_name == "ABAG":
    #         ABAG.append(city_name)
    #     elif agency_name == "SCAG":
    #         SCAG.append(city_name)
        
    # print(SACOG)
    # orgs_to_process = (ABAG + SACOG + SCAG)
    # orgs_to_process = args.agency

    # all_docs = getPaths(orgs_to_process)
    # valid_range = string.ascii_lowercase[:8]
    # all_docs = list(filter(lambda x: "counties/los angeles".lower() in x.lower(), all_docs))
    # all_docs = list(filter(lambda x: "counties/orange".lower() in x.lower(), all_docs))
    # all_docs = list(filter(lambda x: "cities/los angeles".lower() not in x.lower(), all_docs))
    # all_docs = list(filter(lambda x: "cities/los angeles".lower() in x.lower(), all_docs))
    all_docs = []

    for pair in args.pair:
        county_name = pair[0]
        city_name = pair[1]
        source_name = pair[2]

        municipality_path = Path(data_path(county_name, city_name))
        source_output_path = municipality_path / "output" / Path(source_name).stem
        source_output_camelot_path = source_output_path / "camelot"
        source_output_aws_path = source_output_path / "aws"

        if hasXlsxFiles(source_output_camelot_path):
            all_docs.append(source_output_camelot_path)
        elif hasXlsxFiles(source_output_aws_path):
            all_docs.append(source_output_aws_path)
        else:
            raise Exception("Path does not exist: " + str(source_output_path))
          
        # output_docs_dir = glob.glob(data_path(county_name, city_name) + "/output/**", recursive=False)

        # if tables_dir
        
    # all_docs = list(filter(lambda x: "cities/berkeley".lower() in x.lower(), all_docs))
    # all_docs = glob

    # all_docs = [file_path for file_path in all_docs if file_path.split("/cities/")[1].split("/")[0].startswith(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'))]
    # all_docs = [file_path for file_path in all_docs if file_path.split("/cities/")[1].split("/")[0].startswith(('K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'))]
    # all_docs = list(filter(lambda x: "cities/Placerville".lower() in x.lower(), all_docs))
    # all_docs = list(filter(lambda x: "cities/oakland" in x.lower(), all_docs))
    # all_docs = list(filter(lambda x: "cities/livermore" in x.lower(), all_docs))
    # all_docs = list(filter(lambda x: "oakland-6th-draft063022" in x.lower(), all_docs))
    # all_docs = list(filter(lambda x: "beverly-hills-6th-adopted092922" in x, all_docs))
    # all_docs = list(filter(lambda x: "burbank" in x, all_docs))
    # all_docs = list(filter(lambda x: "cities/arcadia" in x.lower(), all_docs))
    # all_docs = list(filter(lambda x: "arcadia-6th-draft083122" in x.lower(), all_docs))
    
    # all_docs = list(filter(lambda x: "cities/petaluma" in x.lower(), all_docs))
    
    # all_docs = list(filter(lambda x: 
    #                         all(substring not in x.lower() for substring in 
    #                         ["counties/orange", "counties/los angeles"]), 
    #                         all_docs ))
    
    # all_docs = random.sample(all_docs, 10)
    # print(all_docs)
    # return
    # parcel_table_name = 'clustered_table'

    # my_apn_datasets = list_tables(PROJECT_ID)
    # my_apn_datasets = list(map(lambda x: x.table_id, my_apn_datasets))
    # my_apn_datasets = list(map(lambda x: x.replace("⁀", "(").replace("‿", ")"), my_apn_datasets))

    # print(my_apn_datasets)
    # meta = list_doc_metadata(PROJECT_ID)

    # For logging purposes
    # accumulator = {
    #     "local": {},
    #     "server": {}
    #     }
    # dfs_bucket = []

    # for path_to_execute_on in sorted(all_docs, key=lambda x: Path(x).name.lower()):
    #     path_to_execute_on = Path(path_to_execute_on)
    #     print(path_to_execute_on)

        
    #     city_name = path_to_execute_on.parent.parent.stem # TODO: This should probably come from Main
    #     county_name = path_to_execute_on.parent.parent.parent.parent.stem # TODO: This should probably come from Main
    #     agency_name = get_agency_from_city_name(city_name)
        
    #     # For logging purposes
    #     # repo_link = "[link](<counties/" + county_name + "/cities/" + city_name + ">)"

    #     df_container = Df_Container(
    #         city_name = city_name,
    #         county_name = county_name,
    #         agency_name = agency_name,
    #         # doc_file_name = path_to_execute_on.stem,
    #         doc_path = path_to_execute_on,
    #         # link = repo_link,
    #         df = None,
    #         server_gdf = None # gdf from server with geometry
    #     )


        
        # input_path = path_to_execute_on.parents[1] / "input" / (path_to_execute_on.stem + ".pdf")
        # print(input_path)
        # print(str(os.path.exists(input_path)))
        # print("----------------------")
        # print(city_name)
        # print(df_container.doc_path.stem)
        # print("----------------------")

        # df_container.df = find_tables_and_parcels(df_container.chosen_path())
        # dfs_bucket.append(df_container)
        # df["table_rows"] = df['table_rows'].apply(lambda x: [remove_special_chars(item['APN']) for item in x])
    
  
    # semaphore_1 = asyncio.Semaphore(1)

    # results_1 = await asyncio.gather(*[
    #     _execute_task(semaphore_1, find_tables_and_parcels_v2, [df_container.chosen_path()], i + 1, len(dfs_bucket)) 
    #     for i, df_container in enumerate(dfs_bucket)
    #     ])
    
    # if len(results_1) != len(dfs_bucket):
    #     raise Exception("server results and bucket are not the same length")
    dfs_bucket = []

    for i, source_output_path in enumerate(all_docs):
        print("task " + str(i + 1) + " of "  + str(len(dfs_bucket) + 1) + " started...")
        print(source_output_path)
        extract_result = find_tables_and_parcels_v2(source_output_path)
        # df_container.df = extract_result
        print(extract_result)
        dfs_bucket.append(extract_result)
        print("task " + str(i + 1) + " of " + str(len(dfs_bucket) + 1) + " completed.")
        # df_container.df.to_json('temp/output.json', orient='records') # For debugging

    # return

    semaphore_2 = asyncio.Semaphore(1)

    # Get intersection from server
    print('Getting intersection...')
    results_2 = await asyncio.gather(*[
        _execute_task(semaphore_2, generate_request, [df_container, False], i + 1, len(dfs_bucket)) 
        for i, df_container in enumerate(dfs_bucket)
        ])
    
    for i, df_container in enumerate(dfs_bucket):
        generate_request(df_container, False)

    if len(results_2) != len(dfs_bucket):
        raise Exception("server results and bucket are not the same length")

    for i, df_container in enumerate(dfs_bucket):
        df_container.server_gdf = results_2[i]

        # print('done! now writing to output_server.json')
        # Write to a temp file for debugging
        # with open('temp/output_server.json', 'w') as f:
        #     f.write(df_container.server_gdf.to_json())

    # raise Exception("Great job!")

    # If args.save is True, then generate save fies and save them to the output directory
    if args.save == True:
        print("generating shapefiles...")
        
        for df_container in dfs_bucket:
            generate_shapefile(df_container.server_gdf, df_container.shapefile_output_dir())


        data_for_markdown = Df_Container.generate_data_for_markdown(dfs_bucket)
        data_for_markdown.sort(key=lambda x: (x['agency'], x['city']))

        city_groups = bucket(data_for_markdown, key=lambda x: x["agency"])

        for key in list( city_groups ):
            city_group = list( city_groups[key] )
            column_headers = list( city_group[0].keys() )
            values = list(map(lambda x: list(x.values()), city_group) )

            writer = MarkdownTableWriter(
                    headers=column_headers,
                    value_matrix=values,
                )
            
            markdown_table_string = "# " + city_group[0]["agency"] + '\n' + writer.dumps() + '\n'
            with open("./README.md", 'a') as file:
                file.write(markdown_table_string)


   


    print("completely done!")

    return

if __name__ == '__main__':
    asyncio.run(main())

