import os
import glob
import json
import geopandas as gpd
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path('.env.local'))

TEST_FILE_PATH_1 = os.getenv('TEST_FILE_PATH_1')
COUNTIES_DIR_PATH = os.getenv('COUNTIES_DIR_PATH')
MAIN_FILE_PATH = os.getenv('MAIN_FILE_PATH')

def printer(count_list):
    print(str(count_list[0]) + " done")
    print(str(count_list[1]) + " partially done")
    print(str(count_list[2]) + " not done at all")
    print(str(count_list[3]) + " can't be done because there's no input data")

def count_city_status(cities):
    results = [0, 0, 0, 0]
    for city in cities:
        name = city["city"]
        county = city["county"]
        # planning_agecy = city["planning_agency"]
        
        input_path = os.path.join(COUNTIES_DIR_PATH, county, "cities", name, "input")
        output_path = os.path.join(COUNTIES_DIR_PATH, county, "cities", name, "output")

        if os.path.exists(input_path):
            pdf_files = glob.glob(os.path.join(input_path, '*.pdf'))
            pdf_files_without_extension = [os.path.splitext(os.path.basename(path))[0] for path in pdf_files]
            pdf_files_count = len(pdf_files)
            if (pdf_files_count == 0):
                results[3] += 1
            else:
                output_dirs_count = 0
                output_dir_exists = os.path.exists(output_path)

                if output_dir_exists:
                    outputs = os.listdir(output_path)
                    for item in outputs:
                        # input_file_without_extension = os.path.splitext(item)[0]
                        # item_path = os.path.join(directory, item)
                        # print(input_file_without_extension)
                        # print(outputs)
                        # matches = len([s for s in outputs if input_file_without_extension in s])
                        # print(pdf_files_without_extension)
                        if item in pdf_files_without_extension and os.path.isdir(os.path.join(output_path, item)):
                            output_dirs_count += 1
                
                
                # xlsx_files_count = len(glob.glob(os.path.join(output_path, '*.xlsx')))
                # csv_files_count = len(glob.glob(os.path.join(output_path, '*.csv')))


                
                if (pdf_files_count == output_dirs_count):
                    results[0] += 1
                elif output_dirs_count > 0:
                    results[1] += 1
                elif output_dirs_count == 0:
                    results[2] += 1
        else:
            results[3] += 1


    return results

def main():

    with open(MAIN_FILE_PATH, 'r') as file:
        main_data = json.load(file)
    
    abag_cities = [x for x in main_data if x["planning_agency"] == "ABAG" ]
    sacog_cities = [x for x in main_data if x["planning_agency"] == "SACOG" ]
    sandag_cities = [x for x in main_data if x["planning_agency"] == "SANDAG" ]
    scag_cities = [x for x in main_data if x["planning_agency"] == "SCAG" ]

    # abag_fully_completed_cities = 0
    # abag_partially_completed_cities = 0
    # sacog_fully_completed_cities = 0
    # sacog_partially_completed_cities = 0
    # sandag_fully_completed_cities = 0
    # sandag_partially_completed_cities = 0
    # scag_fully_completed_cities = 0
    # scag_partially_completed_cities = 0

    abag_count = count_city_status(abag_cities)
    sacog_count = count_city_status(sacog_cities)
    sandag_count = count_city_status(sandag_cities)
    scag_count = count_city_status(scag_cities)

    print("ABAG count: ")
    printer(abag_count)
    print("-----------")
    print("SACOG count: ")
    printer(sacog_count)
    print("-----------")
    # print("SANDAG count: ")
    # printer(sandag_count)
    # print("-----------")
    print("SCAG count: ")
    printer(scag_count)
    print("-----------")
    


    # for city in abag_cities:
    #     name = city["city"]
    #     county = city["count"]
    #     planning_agecy = city["planning_agency"]
        
    #     input_path = os.join(counties_path_name, county, "cities", name, "input")
    #     output_path = os.join(counties_path_name, county, "cities", name, "output")

    #     if os.path.exists(input_path) and os.path.exists(output_path):
    #         pdf_files_count = len(glob.glob(os.path.join(input_path, '*.pdf')))
    #         xlsx_files_count = len(glob.glob(os.path.join(output_path, '*.xlsx')))
    #         csv_files_count = len(glob.glob(os.path.join(output_path, '*.csv')))
    #         if (pdf_files_count == (xlsx_files_count + csv_files_count)):

    return

if __name__ == '__main__':
    main()