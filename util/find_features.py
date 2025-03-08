import geopandas as gpd
import pandas as pd
import shutil
import os
import glob
import warnings
from pathlib import Path
from send2trash import send2trash
import pyogrio

def filter_cities(city_path, counties_to_search, city_names_to_search):
    # Filter cities by county
    # cities = cities[cities['County'] == 'Napa']
    # print(cities)
    # print(cities['Municipality'])
    # if city_path.parts[-1] == "Oakland":
    #     print(city_names_to_search)
    #     if "Oakland" not in city_names_to_search:
    #         raise Exception("Oh no!")
    #     raise Exception("Oakland")
    
    if city_path.parts[-3] in counties_to_search and city_path.parts[-1] in city_names_to_search:
        return True

    return False
def find_features(cities_to_search=None):
  
    cities_dirs = glob.glob('counties/*/cities/*', recursive=False) #TODO: should be relative to repo root
    cities = list(map(lambda x: Path(x), cities_dirs))
    
    # Check if there is a filter
    if cities_to_search != None:
        
        counties_to_search = []
        city_names_to_search = []

        for city in cities_to_search:
            counties_to_search.append(city[0])
            city_names_to_search.append(city[1])

        # print(city_names_to_search)
        # print("Filtering cities to search")
        # print(cities)
        cities = list(filter(lambda x: filter_cities(x, counties_to_search, city_names_to_search), cities))
        
    # print(cities)

    # dupes = set()
    municipalities = []
    missing_parcels = []
    
    for city in cities:
        feature_count = 0
        city_name = city.name
        county_name = city.parts[-3]
        # print(city_name)
        # shp = city / "output" / "misc" / "shapefile.zip"
        # if city.name != "American Canyon":
        #     continue
        # print("ok")
        output_dir = city / "output"
        output_dir_contents = glob.glob(str(output_dir) + "/**/misc", recursive=False)

        # If city doesn't have an output directory or an empty output directory, add it to the missing_parcels list
        if not output_dir.exists or len(output_dir_contents) == 0:
            missing_parcels.append(city.name)

            # continue

        for dir in output_dir_contents:
            dir = Path(dir)
            shp = dir / "shapefile.zip"
            num_features = 0
            
            if shp.exists():
                # missing_parcels.append(city.name)
                # print("Shapefile not found in " + str(dir))
                # continue
            
                # Open the shapefile
                dataset = pyogrio.read_dataframe(str(shp))

                # Count the number of features (rows)
                
                num_features = len(dataset)

                if city_name == "American Canyon":
                    print("dataset")
                    print(dataset)
                # print(shp.parent.parent.name + " " + str(num_features))
                feature_count += num_features

                if num_features == 0:
                    missing_parcels.append(city.name)
                    # print("no features found in " + str(shp))
                    # continue
                # print("num_features: " + str(num_features))
        
        
            municipalities.append({"County": county_name, "Municipality": city_name, "Features_Count": num_features})
            # print(city.name + " " + str(city_count))
            # if city_name == "American Canyon":
            #         print({"County": county_name, "Municipality": city_name, "Features_Count": num_features})
            #         raise Exception("American Canyon")
    
    
    df = pd.DataFrame(municipalities)
    # print(df)
    df = df.groupby(['County', 'Municipality'], as_index=False)['Features_Count'].sum()
    # print(df)
    # print(df)
    return df


if __name__ == "__main__":
    find_features()