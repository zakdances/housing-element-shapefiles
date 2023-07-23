import os
import shutil
import glob
from pathlib import Path
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

COUNTIES_DIR_PATH = Path(os.getenv('COUNTIES_DIR_PATH'))

columns = ['table_name', 'table_order', 'table_rows']
columns_nested = ['APN', 'page_number', 'row_number']

search_terms = ['APN', 'Assessor']
negative_search_terms = ['Identification', 'identifier']

def is_apn_table(df):
    

    for col in df.columns:
        match_1 = any(term in col for term in search_terms)
        match_2 = not any(term in col for term in negative_search_terms)
        if match_1 and match_2:
            return str(col)
    return False
    
def main():
    glob_path = str(COUNTIES_DIR_PATH.resolve()) + "/*" + "/cities" + "/*" + "/output" + "/*"
    dirs = glob.glob(glob_path)
    # for dir in dirs:
    #     xlsx_files = glob.glob(os.path.join(dir, "*.xlsx"))
    #     for xlsx_file in xlsx_files:
    #         shutil.move(xlsx_file, dir + "/aws")
    #         print("moved!")

        # print(str(len(xlsx_files)))
            # if not os.path.exists(dir + "/aws"):
            #     os.makedirs(dir + "/aws")
            #     print('created!')

    # print(dirs)
    return

if __name__ == '__main__':
    main()