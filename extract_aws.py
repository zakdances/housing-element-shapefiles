import os
import glob
import json
import random
import time

import boto3
from textractor import Textractor
from textractor.data.constants import TextractFeatures
import concurrent.futures
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path('.env.local'))

# Create a Textract client
client = boto3.client('textract')

# Get the path to the local file
COUNTIES_DIR_PATH = os.getenv('COUNTIES_DIR_PATH')
MAIN_FILE_PATH = os.getenv('MAIN_FILE_PATH')


# Define your tasks as functions
def make_job(task_id, input_file_path, output_file_dir):
    extractor = Textractor(profile_name="default")

    print(f"Task {task_id} started: " + input_file_path)
    document = extractor.start_document_analysis(
        file_source=input_file_path,
        s3_upload_path="s3://housingelements",
        features=[TextractFeatures.TABLES]
    )
    print(f"Task {task_id}: " + "Upload complete")
    
    return document


def main():
    

    # make_job(extractor)

    with open(MAIN_FILE_PATH, 'r') as file:
        main_data = json.load(file)
    
    filtered_list = list(filter(lambda x: x["planning_agency"] == "ABAG", main_data))
    filtered_list = random.sample(filtered_list, 30)


    task_queue = []
    for city in filtered_list:
        city_name = city["city"]
        county_name = city["county"]
        # urls = city["housing_element"]

        city_dir_path = os.path.join(COUNTIES_DIR_PATH, county_name, "cities", city_name)
        input_dir_path = os.path.join(city_dir_path, "input")
        output_dir_path = os.path.join(city_dir_path, "output")
        pdf_file_paths = glob.glob(input_dir_path + '/*.pdf')

        for pdf_file_path in pdf_file_paths:
            filename = os.path.basename(pdf_file_path)
            filename_without_extension = os.path.splitext(filename)[0]
            output_file_dir = os.path.join(output_dir_path, filename_without_extension)
            task = (str(len(task_queue) + 1), pdf_file_path, output_file_dir)

            if os.path.exists(output_file_dir):
                print("skipping " + output_file_dir)
            else:
                task_queue.append(task)


    # Create a task queue
    # task_queue = [(1, 'A', True), (2, 'B', False), (3, 'C', True), (4, 'D', False), (5, 'E', True)]  # Example: 20 tasks

    # Create a ThreadPoolExecutor with a maximum of 5 workers
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks to the executor
        # future_to_task = {executor.submit(task_function, task_id): task_id for task_id in task_queue}
        future_to_task = {}
        for arg1, arg2, arg3 in task_queue:
            task_args = (arg1, arg2, arg3)
            future = executor.submit(make_job, *task_args)
            future_to_task[future] = task_args

        # Process the completed tasks as they finish
        for future in concurrent.futures.as_completed(future_to_task):
            # print("Donner")
            task_args_of_future = future_to_task[future]
            task_id = task_args_of_future[0]
            # print("Donner: " + task_id)
            try:
                print("Task " + str(task_id) + " ready for post-process")
                # Get the result of the completed task
                document = future.result()
                tables = document.tables
                print("Task " + str(task_id) + " tables: " + str(len(tables)))

                tables_found_and_added = 0
                os.makedirs(output_file_dir, exist_ok=True)
                # Saves the table in an excel document for further processing
                for i, table in enumerate(tables):
                    page = table.page
                    page_id = table.page_id
                    # print("table found on page " + str(page))
                    # table.to_excel("output.xlsx")
                    output_filename = "table_" + str(page) + "_" + str(page_id) + "_" + str(i + 1) + ".xlsx"
                    output_file_path = os.path.join(output_file_dir, output_filename)
                    table.to_excel(output_file_path)
                    tables_found_and_added += 1

                print(f"Task {task_id} completed")
                print("tables found and added: " + str(tables_found_and_added))
                print(output_file_dir)
                # time.sleep(15)

            except Exception as exc:
                # Handle any exceptions that occurred during task execution
                print(f"Task {task_id} generated an exception: {exc}")
            else:
                # Process the task result (if needed)
                print("Done with task...really, this time!")
                pass
    print("great! got here")

if __name__ == '__main__':
    main()