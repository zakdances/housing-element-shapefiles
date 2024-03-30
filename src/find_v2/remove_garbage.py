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

# columns = ['table_name', 'table_order', 'table_rows']
# columns_nested = ['APN', 'page_number', 'row_number']

# search_terms = ['APN', 'Assessor']
# negative_search_terms = ['Identification', 'identifier']

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

def remove_garbage(target_string, sample=None):
    target_string = str(target_string)
    target_string = target_string.replace(".", " ")
    target_string = target_string.replace("|", " ")
    target_string = target_string.replace("\n", " ")
    target_string = target_string.replace("/", " ").replace("\\", " ")
    
    for zip_code in zip_codes:
        if zip_code in target_string:
            target_string = target_string.replace(zip_code, " ")
            # print("found a zip")
            # print(target_string)

    target_string_split = target_string.split(" ")

    new_string = ""
    for string in target_string_split:
        if len(string.strip()) > 0:
            new_string += string + " "
    new_string = new_string.strip()
    new_string = new_string.strip(',;)')
    # if len(new_string) == 0:
    #     return ""

    # if sample:
    #     sample = sample.strip()
    #     if sample.count(" ") != new_string.count(" "):
    #         print("sample corrected!")
    #         print(sample)
    #         print(new_string)
    #         new_string = get_longest_word(new_string)

    return new_string