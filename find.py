import os
import glob
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

load_dotenv(dotenv_path=Path('.env.local'))

CALIFORNIA_ZIP_CODES_FILEPATH = os.getenv('CALIFORNIA_ZIP_CODES_FILEPATH')

columns = ['table_name', 'table_order', 'table_rows']
columns_nested = ['APN', 'page_number', 'row_number']

search_terms = ['APN', 'Assessor']
negative_search_terms = ['Identification', 'identifier']

with open(CALIFORNIA_ZIP_CODES_FILEPATH, 'r') as file:
    zip_data = json.load(file)

zip_codes = list(map(lambda x: str(x['properties']['ZIP_CODE']), zip_data['features']))


def get_longest_word(input_string):
    input_string = str(input_string)
    if len(input_string.strip()) == 0:
        return ""
    words = input_string.split()  # Split the input string into words
    longest_word = max(words, key=len)  # Find the longest word using the 'max' function with 'key=len'
    return longest_word

def is_apn_table(df):
    
    for col in df.columns:
        # print(remove_garbage(col))
        # col = remove_garbage(col)
        match_1 = any(term in col for term in search_terms)
        match_2 = not any(term in col for term in negative_search_terms)

        if match_1 and match_2:
            # print(df.columns)
            return str(col)
    
    return False

def remove_garbage(target_string, sample=None):
    target_string = str(target_string)
    target_string = target_string.replace("/", " ").replace("\\", " ")
    target_string_split = target_string.split(" ")
    new_string = ""
    for string in target_string_split:
        if string not in zip_codes and len(string.strip()) > 0:
            new_string += string + " "
    new_string = new_string.strip()
    # if len(new_string) == 0:
    #     return ""

    if sample:
        # print("sample found!")
        sample = sample.strip()
        if sample.count(" ") != new_string.count(" "):
            # print("sample corrected!")
            new_string = get_longest_word(new_string)

    return new_string.strip()


def firstApnRowOfLastTable(df):
    last_row = df.iloc[-1]
    # first_nested_row = last_row[columns[2]][0]
    # print("firstApnRowOfLastTable")
    # print(first_nested_row)
    page_number = pageNumberOfFirstNestedRow(last_row)
    # print("page_number")
    # print(str(page_number))
    return page_number

def pageNumberOfFirstNestedRow(row):
    first_nested_row = row[columns[2]][0]
    page_number = first_nested_row[columns_nested[1]]
    return page_number

def lowestPageNumberOfRow(row):
    nested_rows = row[columns[2]]
    lowest_page_number = 10000000 # TODO: This is so goofy
    for nested_row in nested_rows:
        page_number = nested_row[columns_nested[1]]
        page_number_int = int(page_number)
        if page_number_int < lowest_page_number:
            lowest_page_number = page_number_int

    return str(lowest_page_number)

def highestPageNumberOfRow(row):
    nested_rows = row[columns[2]]
    highest_page_number = 0
    for nested_row in nested_rows:
        page_number = nested_row[columns_nested[1]]
        page_number_int = int(page_number)
        if page_number_int > highest_page_number:
            highest_page_number = page_number_int

    return str(highest_page_number)

def apnValueOfFirstNestedRow(row):
    first_nested_row = row[columns[2]][0]
    apn = first_nested_row[columns_nested[0]]
    return apn

def are_values_similar(str1, str2):
    str1 = str(str1)
    str2 = str(str2)
    same = abs(len(str1) - len(str2)) <= 2
    # TODO: More should go here
    return same

def sort_excel_files_by_page_number(lst):
    return sorted(lst, key=lambda x: x.split("_")[1])


def find_tables_and_parcels(city_output_directory):
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
        
        # Read the Excel file
        df = pd.read_excel(excel_doc_filepath)
        excel_doc_filename = os.path.basename(excel_doc_filepath)
        page_number = excel_doc_filename.split("_")[1]
        found_apn_column = is_apn_table(df)
        apn_sample = None
        is_continuation_of_previous_apn_table = False
        index_of_important_row = 0

        # If a table doesn't have an APN column title, check if its a continuation of the last
        if not found_apn_column:
            for index, row in new_df.iterrows():
                another_page_number = highestPageNumberOfRow(row)
                # print(str(another_page_number) + " " + str(page_number))
                if int(another_page_number) + 1 == int(page_number):
                    print("continuation found! " + page_number)
                    
                    apn_sample = apnValueOfFirstNestedRow(row)
                    # for index_2, incoming_row in df.iterrows():
                    for column_name_2, value_2 in df.iloc[0].items():
                        print(f"{column_name_2}: {remove_garbage(value_2, apn_sample)}")
                        
                        cleaned_possible_apn = remove_garbage(value_2, apn_sample)
                        if are_values_similar(apn_sample, cleaned_possible_apn):
                            # Create a new DataFrame with the column titles as a row
                            new_row = pd.DataFrame([df.columns], columns=df.columns)
                            # Append the new row to the original DataFrame
                            df = pd.concat([new_row, df], ignore_index=True)
                            found_apn_column = column_name_2
                            index_of_important_row = index
                            is_continuation_of_previous_apn_table = True
                            break
                    break


        
        apns_list = []
        

        if found_apn_column:
            
            if is_continuation_of_previous_apn_table == False:
                
                apn_table_found_with_table_name = "table_" + str(len(new_df))
                new_row = {}
                new_row[columns[0]] = apn_table_found_with_table_name
                new_row[columns[1]] = len(new_df)
                new_row[columns[2]] = []
            

                # Retrieve the last row using the index
                # matching_row_index = len(new_df) - 1

                # matching_rows = new_df[new_df[columns[0]] == apn_table_found_with_table_name]
                # matching_row_index = None

                # if len(matching_rows) > 0:
                #     matching_row_index = matching_rows.index[0]
                # else:
                #     new_row = {}
                #     new_row[columns[0]] = apn_table_found_with_table_name
                #     new_row[columns[1]] = len(new_df)
                #     new_row[columns[2]] = []
                #     # new_df = new_df.append(new_row, ignore_index=True)
                new_df = pd.concat([new_df, pd.DataFrame([new_row])], ignore_index=True)
                index_of_important_row = len(new_df) - 1
            else:
                apns_list = new_df.at[index_of_important_row, columns[2]]
                # print("here: ")
                # print(apns_list)
                

            # if matching_row_index == None:
            #     raise TypeError("Invalid value for matching_row_index. " + str(matching_row_index))


            # apns_df = pd.DataFrame(columns=columns_nested)
            # apns_list = []

            # Loop through all rows
            for index, row in df.iterrows():
                # print("addresses_list: ")
                # Access the "addresses" column as a list
                # addresses_df = new_df.loc[matching_row_index][columns[2]]
                # print(type(addresses_df))
                new_apn = row[found_apn_column]
                new_apn = str(new_apn) if isinstance(new_apn, (int, float, complex)) else new_apn
                new_apn = remove_garbage(new_apn, apn_sample)

                new_nested_row = {}
                new_nested_row[columns_nested[0]] = new_apn
                new_nested_row[columns_nested[1]] = page_number
                new_nested_row[columns_nested[2]] = len(apns_list)
                
                if isinstance(new_apn, str) and not new_apn.lower().strip() == "nan" and not new_apn.isspace() and len(new_apn) > 0:
                    # apns_df = pd.concat([apns_df, pd.DataFrame([new_nested_row], columns=columns_nested)], ignore_index=True)
                    if apn_sample == None or are_values_similar(new_apn, apn_sample) == True:
                        apns_list.append(new_nested_row)

            # new_thing = apns_df.values.tolist()
            # new_thing2 = apns_df.to_records()
            # print(apns_df)
            new_df.at[index_of_important_row, columns[2]] = apns_list
            # print(f"An apn table with {str(len(apns_list))} apns found in: " + excel_doc_filename)
            # addresses_df = new_df.loc[matching_row_index][columns[2]]
            # addresses_df.extend(new_thing)
            
    # print("new_df")
    # print(new_df)
    
    for index, row in new_df.iterrows():
        apns = row[columns[2]]
        lowest_page = lowestPageNumberOfRow(row)
        higheset_page = highestPageNumberOfRow(row)
        print(f"An apn table with {str(len(apns))} apns found from page {str(lowest_page)} to {str(higheset_page)}")
    return new_df

if __name__ == '__main__':
    find_tables_and_parcels()