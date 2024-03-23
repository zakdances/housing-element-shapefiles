import os
import glob
import re
import asyncio
from functools import reduce
from enum import Enum
from time import sleep
import json
import jsonlines
import random
import geopandas as gpd
import pandas as pd
import numpy as np
from pathlib import Path
from dotenv import load_dotenv

from .column_titles import columns, columns_nested
from .remove_garbage import remove_garbage
from .highest_page_number_of_row import highest_page_number_of_row
from .lowest_page_number_of_row import lowest_page_number_of_row
from .pull_possible_apn_from_cell_value import pull_possible_apns_from_cell_value

load_dotenv(dotenv_path=Path('.env.local'))

# CALIFORNIA_ZIP_CODES_FILEPATH = os.getenv('CALIFORNIA_ZIP_CODES_FILEPATH')

search_terms = ['APN', 'Assessor', 'Parcel Number']
negative_search_terms = ['Identification', 'identifier']

# with open(CALIFORNIA_ZIP_CODES_FILEPATH, 'r') as file:
#     zip_data = json.load(file)

# zip_codes = list(map(lambda x: str(x['properties']['ZIP_CODE']), zip_data['features']))


def is_probably_apn(possibly_apn, sample=None):
    possibly_apn = remove_garbage(possibly_apn)
    numbers_in_string = len(re.findall(r'\d', possibly_apn))
    apn_found_most_likely = False

    # if possibly_apn == "027-062-02":
    #     print("great, got there")
    #     print(len(re.findall(r'\d', possibly_apn)))

    if numbers_in_string > 5 and len(possibly_apn) >= 7 and len(possibly_apn) < 25:
        if sample:
            sample = remove_garbage(sample)
            if len(sample) == 0:
                raise Exception("Invalid data: 0 length sample")
            apn_found_most_likely = abs(len(possibly_apn) - len(sample)) <= 2
        else:
            apn_found_most_likely = True
    if "$" in possibly_apn:
        apn_found_most_likely = False


    return apn_found_most_likely

def find_apn_sample_in_excel_table(df, test_page_number):
    test_page_number = int(test_page_number)
    row_search_tolerance = 10
    is_apn_table = False
    sample = None
   
    # if test_page_number == 395:
    #     print("here we go")
    
    for index, row in df.head(5).iterrows():
      
        # 'index' is the row index, and 'row' is a pandas Series representing the row data
        # You can access the values of each column using row['column_name']
        # Example: print(row['column_name'])
        for column, cell_value in row.items():
            cell_value = remove_garbage(cell_value)

            # if test_page_number == 734:
            #     print(cell_value)
            
            for search_term in search_terms:
                if search_term.lower() in cell_value.lower():
                    # print("found success")
                    # if len(cell_value) < 30:
                    #     print(cell_value.lower())
                    
                    is_apn_table = True
    
    if is_apn_table == True:
        for index, row in df.head(row_search_tolerance).iterrows():
            for column, cell_value in row.items():
                cell_value = remove_garbage(cell_value)
                possible_apns = pull_possible_apns_from_cell_value(cell_value)
                for possible_apn in possible_apns:
                    if is_probably_apn(possible_apn):
                        sample = possible_apn
                        break
                if sample:
                    break
    
    return sample

def firstApnRowOfLastTable(df):
    last_row = df.iloc[-1]
    # first_nested_row = last_row[columns[2]][0]
    # print("firstApnRowOfLastTable")
    # print(first_nested_row)
    apn = apn_value_of_first_nested_row(last_row)
    # print("page_number")
    # print(str(page_number))
    return apn

def apn_value_of_first_nested_row(row):
    first_nested_row = row[columns[2]][0]
    apn = first_nested_row[columns_nested[0]]
    return apn

# def apnValueOfFirstNestedRow(row):
#     first_nested_row = row[columns[2]][0]
#     apn = first_nested_row[columns_nested[0]]
#     return apn

def are_values_similar(str1, str2):
    str1 = str(str1)
    str2 = str(str2)
    same = abs(len(str1) - len(str2)) <= 2
    # TODO: More should go here
    return same

def sort_excel_files_by_page_number(lst):
    # Function to extract numbers from the file name using split("_")
    def extract_numbers(filename):
        filename = Path(filename).name
        numbers = filename.split("_")
        primary_key = int(numbers[1])
        
        # Some filenames may have additional periods due to the file extension,
        # so we need to remove the extension to extract the secondary key
        secondary_key_with_extension = numbers[3]
        secondary_key = int(secondary_key_with_extension.split(".")[0])
        
        return primary_key, secondary_key

    return sorted(lst, key=extract_numbers)


async def find_tables_and_parcels(city_output_directory):
    # await asyncio.sleep(0.25)

    formatted_rows = []

    excel_doc_filepaths = [
        os.path.join(city_output_directory, excel_doc)
        for excel_doc in os.listdir(city_output_directory)
        if excel_doc.endswith(".xlsx")
    ]
    excel_doc_filepaths = sort_excel_files_by_page_number(excel_doc_filepaths)


    new_df = pd.DataFrame(columns=columns)
    rows = []

    for excel_doc_filepath in excel_doc_filepaths:

        excel_doc_filename = os.path.basename(excel_doc_filepath)
        page_number = excel_doc_filename.split("_")[1]

        # Read the Excel file
        df = pd.read_excel(excel_doc_filepath, header=None)
        # last_row = new_df.iloc[-1] if len(new_df) > 0 else None
        is_table_next_to_previous_apn_table = False
        apn_sample = None

        if len(new_df) > 0:
            last_row = new_df.iloc[-1]
            nearest_previous_page_number = highest_page_number_of_row(last_row)
            is_table_next_to_previous_apn_table = int(page_number) == int(nearest_previous_page_number) or int(page_number) == int(nearest_previous_page_number) + 1
            if is_table_next_to_previous_apn_table:
                apn_sample = apn_value_of_first_nested_row(last_row)

        if apn_sample == None:
            apn_sample = find_apn_sample_in_excel_table(df, page_number)

        # apn_sample = apn_value_of_first_nested_row(last_row) if last_row
        # apn_sample = apn_value_of_first_nested_row(last_row) if last_row else find_apn_sample_in_excel_table(df)

        # found_apn_column = is_apn_table(df)
        # apn_sample = None
        # is_continuation_of_previous_apn_table = False
        # index_of_important_row = 0

        # If a table doesn't have an APN column title, check if its a continuation of the last
   


        
        apns_list = []
        if is_table_next_to_previous_apn_table == True:
            lastArr = new_df.loc[len(new_df) - 1, columns[2]]
            apns_list = lastArr + apns_list
            # print("got here")
        

        # Loop through all rows and cells
        for index, row in df.iterrows():
            for column, cell_value in row.items():
                # print("addresses_list: ")
                # Access the "addresses" column as a list
                # addresses_df = new_df.loc[matching_row_index][columns[2]]
                # print(type(addresses_df))
                apns_in_cell = []
                # new_apn = cell_value
                cell_value = remove_garbage(cell_value)
                for possible_apn in pull_possible_apns_from_cell_value(cell_value):
                    possible_apn = remove_garbage(possible_apn)

                    # print("sample: ")
                    # print(apn_sample)
                    if apn_sample and is_probably_apn(possible_apn, apn_sample):
                        
                        
                        new_apn = str(possible_apn) if isinstance(possible_apn, (int, float, complex)) else possible_apn
                        # print("found apn: " + str(new_apn))
                        # new_apn = remove_garbage(new_apn, apn_sample)

                        new_nested_row = {}
                        new_nested_row[columns_nested[0]] = new_apn
                        new_nested_row[columns_nested[1]] = page_number
                        new_nested_row[columns_nested[2]] = len(apns_list)
                        
                        if isinstance(new_apn, str) and not new_apn.lower().strip() == "nan" and not new_apn.isspace() and len(new_apn) > 0:
                            # apns_df = pd.concat([apns_df, pd.DataFrame([new_nested_row], columns=columns_nested)], ignore_index=True)
                            if apn_sample == None or are_values_similar(new_apn, apn_sample) == True:
                                apns_list.append(new_nested_row)
                                break

        # new_thing = apns_df.values.tolist()
        # new_thing2 = apns_df.to_records()
        # print(apns_df)
        if len(apns_list) > 0:
            if is_table_next_to_previous_apn_table == False:
                apn_table_found_with_table_name = "table_" + str(len(new_df))
                new_row = {}
                new_row[columns[0]] = apn_table_found_with_table_name
                new_row[columns[1]] = len(new_df)
                new_row[columns[2]] = []
                new_df = pd.concat([new_df, pd.DataFrame([new_row])], ignore_index=True)

            new_df.at[len(new_df) - 1, columns[2]] = apns_list

        # print(f"An apn table with {str(len(apns_list))} apns found in: " + excel_doc_filename)
        # addresses_df = new_df.loc[matching_row_index][columns[2]]
        # addresses_df.extend(new_thing)

            
            
    # print("new_df")
    # print(new_df)
    
    for index, row in new_df.iterrows():
        apns = row[columns[2]]
        lowest_page = lowest_page_number_of_row(row)
        higheset_page = highest_page_number_of_row(row)
        secondary = f"to {str(higheset_page)}" if lowest_page != higheset_page else ""
        print(f"An apn table with {str(len(apns))} apns found on page {str(lowest_page)} {secondary}")
    if len(new_df) == 0:
        print("No apn tables found.")
    return new_df

if __name__ == '__main__':
    find_tables_and_parcels()