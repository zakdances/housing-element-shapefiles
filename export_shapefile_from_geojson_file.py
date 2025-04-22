import geopandas as gpd
import shutil
import os
import glob
import warnings
from pathlib import Path
from send2trash import send2trash
import pyogrio

# ignore RuntimeWarning: Normalized/laundered field name warnings. TODO: This should only effect geojson_to_shapefile
warnings.filterwarnings("ignore", category=RuntimeWarning, module="pyogrio")

def geojson_to_shapefile(geojson_path, output_zip):
    geojson_path = Path(geojson_path)
    output_zip = Path(output_zip)

    if output_zip.suffix != ".zip":
        raise Exception("Output file name must be a ZIP file")

    # Read GeoJSON file
    gdf = gpd.read_file(geojson_path)

    # Define the output Shapefile directory
    # temp_shp_dir = output_zip.parent / "shapefile_output_temp"
    os.makedirs(output_zip.parent, exist_ok=True)

    shapefile_dir_path = output_zip.with_suffix('')
    #Write to Shapefile
    gdf.to_file(shapefile_dir_path, driver='ESRI Shapefile')
    # Create a ZIP file containing all Shapefile components
    shutil.make_archive(shapefile_dir_path, 'zip', shapefile_dir_path)
    # Cleanup the unzipped shapefile
    send2trash(shapefile_dir_path)
    
    # Cleanup intermediate folder
    # shutil.rmtree(shp_dir)

    print("just created a zip file at " + str(shapefile_dir_path.with_suffix('.zip')))
    return shapefile_dir_path.with_suffix('.zip')

def loop(overwrite=False):
    # print(gpd._compat.GEOS_ENGINE)

    # Use the '**' wildcard to recursively search through all subdirectories
    files = glob.glob('counties/**/cities/**/input/*.geojson', recursive=False)
    new_shapefiles_created = []

    # Loop through the list of files
    for file in files:
        file = Path(file)
        
        if file.suffix == ".geojson":
            print(file.parent.parent)
            
            
            output_zip = file.parent.parent / "output" / file.stem / "misc" / "shapefile.zip"

            if overwrite == False and output_zip.exists():
                print("shapefile already exists, skipping")
                continue
            # file.rename(new_file)
            # geojson_to_shapefile(file, file.parent / "output_shapefile.zip") 
            new_shapefile = geojson_to_shapefile(file, output_zip)
            new_shapefiles_created.append(new_shapefile)
            # print("shapefile created at " + str(output_zip))
            # break
    
    print("New shapefiles created:")
    for new_shapefile in new_shapefiles_created:
        print(f"{new_shapefile.stat().st_size / 1024:<20}{str(new_shapefile)}")

# def find_hcd_docs():
#     cities_dirs = glob.glob('counties/**/cities/**', recursive=False)
#     cities = list(map(lambda x: Path(x), cities_dirs))
#     # dupes = set()
#     missing_hcd = []

#     for city in cities:
#         if not (city / "output" / "hcd-011125").exists():
#             missing_hcd.append(city.name)

#     print(missing_hcd)

    # print(list(dupes))

# def find_features():
#     cities_dirs = glob.glob('counties/**/cities/**', recursive=False)
#     cities = list(map(lambda x: Path(x), cities_dirs))
#     # dupes = set()
#     missing_parcels = []

#     for city in cities:
#         city_count = 0
#         # shp = city / "output" / "misc" / "shapefile.zip"
#         # if city.name != "American Canyon":
#         #     continue
#         # print("ok")
#         output_dir = city / "output"
#         output_dir_contents = glob.glob(str(output_dir) + "/**/misc", recursive=False)

#         if not output_dir.exists or len(output_dir_contents) == 0:
#             missing_parcels.append(city.name)
#             continue

#         for dir in output_dir_contents:
#             dir = Path(dir)
#             shp = dir / "shapefile.zip"
            
#             if not shp.exists():
#                 # missing_parcels.append(city.name)
#                 continue
            
#             # Open the shapefile
#             dataset = pyogrio.read_dataframe(str(shp))

#             # Count the number of features (rows)
#             num_features = len(dataset)
#             # print(shp.parent.parent.name + " " + str(num_features))
#             city_count += num_features

#             if num_features == 0:
#                 missing_parcels.append(city.name)
#                 # print("no features found in " + str(shp))
#                 # continue
#             # print("num_features: " + str(num_features))
#         print(city.name + " " + str(city_count))
        

#     print(missing_parcels)
#     print(len(missing_parcels))

def split_geojson(geojson_file_to_be_split):
    gdf = gpd.read_file(geojson_file_to_be_split)
    jurisdiction_name = "jurisdiction_name"
    gdf[jurisdiction_name] = gdf[jurisdiction_name].str.strip()
    gdf[jurisdiction_name] = gdf[jurisdiction_name].str.replace('SAINT HELENA', 'ST. HELENA')
    gdf[jurisdiction_name] = gdf[jurisdiction_name].str.replace('CATHEDRAL', 'CATHEDRAL CITY')
    gdf[jurisdiction_name] = gdf[jurisdiction_name].str.replace('CITY OF MORENO VALLEY', 'MORENO VALLEY')
    gdf[jurisdiction_name] = gdf[jurisdiction_name].str.replace('SAN BUENAVENTURA', 'VENTURA')
    # gdf = gdf[gdf['jurisdiction_name'] != 'SAN BUENAVENTURA']

    name = "hcd-011125.geojson"
    cities_dirs = glob.glob('counties/**/cities/**', recursive=False)
    # cities = list(map(lambda x: Path(x).name.strip().lower(), cities_dirs))
    # jur = gdf['jurisdiction_name'].str.lower().unique().tolist()
    # uniques = set(jur).difference(cities)
    splits = []

    print(len(gdf))
    for city_dir in cities_dirs:
        city_path = Path(city_dir)
        county_name = city_path.parent.parent.name
        
        split_gdf1 = gdf[(gdf['County_Name'].str.upper() == county_name.strip().upper()) & (gdf['jurisdiction_name'].str.upper() == city_path.name.strip().upper())]
       
        if len(split_gdf1) > 0:
            splits.append({ "path": city_path, "split_gdf": split_gdf1 })
            gdf = gdf.drop(split_gdf1.index)
            gdf = gdf.reset_index(drop=True)
    
    if len(gdf) > 0:
        # print(gdf.values.tolist())
        print(gdf['County_Name'].unique().tolist())
        print(gdf['jurisdiction_name'].unique().tolist())
        raise Exception("Mismatch found!")
    
    for split in splits:
        path = split["path"]
        split_gdf = split["split_gdf"] 
        export_path = path / "input" / name

        if not export_path.exists():
            os.makedirs(export_path.parent, exist_ok=True)
            split_gdf.to_file(export_path, driver='GeoJSON')
            print("created: " + str(export_path))
        else:
            print("already exists: " + str(export_path))

    # print(list(uniques))

# Example usage
# geojson_to_shapefile("input.geojson", "output_shapefile.zip")

if __name__ == "__main__":
    # split_geojson("SB6A__pts_Join_3616231054980920121.geojson")
    # loop()
    # find_dupes()
    # find_features()
    pass