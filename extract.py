# import boto3
import json
import os
from pathlib import Path
import glob
import pandas as pd
import numpy as np
import logging
# from botocore.exceptions import ClientError
from ctypes.util import find_library
# import tkinter
import camelot
import tabula
import pdfplumber
from pypdf import PdfReader
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
load_dotenv(dotenv_path=Path('.env.local'))

TEST_FILEPATH_1 = os.getenv('TEST_FILEPATH_1')
COUNTIES_DIR_PATH = Path(os.getenv('COUNTIES_DIR_PATH'))

# files_to_ignore = ["Lafayette-6th-Adopted-013123.pdf", 
#                    "Concord-6th-Adopted-032123.pdf", 
#                    "concord-6th-draft081622.pdf",
#                    "Orinda-6th-Draft-111622.pdf",
#                    "Orinda-6th-Adopted-020123.pdf",
#                    "antioch-6th-draft070122.pd"]
files_to_ignore = ["Oakland-6th-Adopted-021323.pdf"]
# start_page_for_oakland = 4639

def is_directory_empty(directory_path):
    for entry in os.listdir(directory_path):
        if not entry.startswith('.') and entry != '.DS_Store':
            return False
    return True

def log_extract_errors(filepath, errors):
    # print("recording error log...")
    filepath = Path(filepath)
    # Step 1: Read the JSON file
    with open('extract_error_log.json', 'r') as file:
        data = json.load(file)

    # Step 2: Edit the data
    data[filepath.name] = {
        "filepath": str(filepath.resolve()),
        "errors": errors
    }

    # Step 3: Write the updated data back to the file
    with open('extract_error_log.json', 'w') as file:
        json.dump(data, file, indent=2)
    return

def extract_that_file(filepath, output_dir_path, self_limit=None):
    filepath = Path(filepath)
    output_dir_path = Path(output_dir_path)
    tables_container = []
    errors = []


    reader = PdfReader(filepath.resolve())
    page_count = len(reader.pages)
    # print(page_count)

    print("extracting " + filepath.name + "... " + f"({str(page_count)} pages)")
    for i in range(page_count):
        page_number = i + 1
        print("page " + str(page_number) + " of " + str(page_count) + "...")

        # if filepath.name == "oakland-6th-draft120722.pdf" and page_number < start_page_for_oakland:
        #     print("skipping")
        #     continue
        # elif filepath.name == "MenloPark-6th-Adopted-020823.pdf" and page_number < 2000:
        #     print("skipping")
        #     continue
        if self_limit and page_number != int(self_limit):
            continue
        elif page_count > 3000 and page_number < page_count - 2000:
            # print("skipping")
            continue
        


        try:
            tables = camelot.read_pdf(str(filepath.resolve()), pages=str(page_number), flavor='stream')
            tables_container.append(tables)

        except Exception as e:
            # print("An unexpected error occurred:", e)
            errors.append({"page_number": page_number, "error_message": str(e)})
        
        # if i == 5:
        #     break

    # print("extracting " + filepath.name + "...")
    # tables = camelot.read_pdf(str(filepath.resolve()), pages='1-end', flavor='stream')
    # print("Total tables extracted:", tables.n)


    if list(filter(lambda x: x.n > 0, tables_container)) and not output_dir_path.exists():
        output_dir_path.mkdir(parents=True)

    iteration = 0
    for index, tables in enumerate(tables_container):
        for index_2, table in enumerate(tables):
            
            new_name = f"table_{str(table.page)}_placeholder-id_{str(iteration)}"
            new_filename = new_name + ".xlsx"
            new_output_path = output_dir_path / new_filename

            df = table.df
            df.to_excel(new_output_path.resolve())
            iteration += 1
    
    print("Wrote " + str(iteration) + " tables to disk.")
    if errors:
        print(str(len(errors)) + " errors logged.")
        log_extract_errors(filepath, errors)
    # print("done with " + str(tables.n) + " tables")

def main():


    # find_library("gs")


    # return

    glob_path = str(COUNTIES_DIR_PATH.resolve()) + "/*" + "/cities" + "/*"
    city_dirs = glob.glob(glob_path)


    for dir in city_dirs:
        # print(dir)
        dir = Path(dir)
        input_dir_path = dir / "input"
        output_dir_path = dir / "output"
        
        # new_glob = glob.glob(dir + "/output" + "/*" + "/aws")
        if input_dir_path.exists():
            for input_file in os.listdir(input_dir_path):
                input_file_filepath = input_dir_path / input_file
                if input_file_filepath.suffix.lower() == ".pdf":
                    # print("pdf found")

                    input_file_output_aws_dir = output_dir_path / input_file_filepath.stem / "aws"
                    input_file_output_camelot_dir = output_dir_path / input_file_filepath.stem / "camelot"

                    if not input_file_output_aws_dir.exists() and not input_file_output_camelot_dir.exists():
                        print("no aws or camelot")
                        # print(input_file_output_camelot_dir.resolve())
                        if not input_file_filepath.name in files_to_ignore:
                            extract_that_file(input_file_filepath, input_file_output_camelot_dir)

                    # else:
                    #     print("aws found")

                    # aws_path = 
                    # if os.path.exists(aws_path):


                # hmm = output_dir_path + "/" + file_output_dir_path
                # aws_path = hmm + "/aws"
                # if os.path.exists(aws_path):
                #     if is_directory_empty(aws_path):
                #         raise ValueError("aws directory empty")
                # else:
                #     if file_output_dir_path != ".DS_Store":
                #         print("output dir but no aws dir for " + file_output_dir_path)

        # else:
        #     print("no input dir for " + "/".join(Path(dir).parts[-3:]))


    return

    # tables = tabula.read_pdf(test_file_path, pages="all")

    # with pdfplumber.open(test_file_path) as pdf:
    #     page = pdf.pages[611]
    #     table = page.extract_table()  # Extract the table as a list of lists
    #     print(table)
    #     # print(first_page.chars[0])
    return

if __name__ == '__main__':
    main()
