import os
import glob
import shutil
from send2trash import send2trash
from pathlib import Path
from data_path import data_path
import geopandas as gpd


def create_shapefiles_from_geojson():

    paths = glob.glob(data_path("*", "*"))
    
    print("opening geodatabase...")
    dfp = gpd.read_file('/Users/zacdean/projects/Upzone/Parcels GIS shapefiles/USA/states/California/counties/Los Angeles/LACounty_Parcels.gdb')
    print("done")
    print(dfp.head(200))

    for col in dfp.columns:
        print(col)

    return

    geojson_path = Path("./temp/HCD/oct")

    if not geojson_path.exists():
        raise Exception("GeoJSON path does not exist: " + str(geojson_path))
    
    geojson_file_paths = list(geojson_path.iterdir())

    
    # for item in geojson_file_paths:
        # print(item)
        # df_from_dir = gpd.read_file(item)



    # return

    for path in paths:
        p = Path(path)
        city = p.name
        county = p.parts[-3]
        output_dir = p / "output" / "hcd-102725" / "misc"

        if city != "Los Angeles" or county != "Los Angeles":
            continue

        # if output_dir.exists():
        #     print("output dir already exists, skipping: " + str(output_dir))
        #     continue

        

        print("----- " + city + ", " + county)

        

        df = None

        for item in geojson_file_paths:
            # print(item)
            df_from_dir = gpd.read_file(item)

            # for col in df_from_dir.columns:
            #     print(col) AssessorParcelNumber APN
                
            df_from_dir.loc[
                (df_from_dir["jurisdiction_name"].str.upper() == "CATHEDRAL") &
                (df_from_dir["County_Name"].str.upper() == "RIVERSIDE"),
                "jurisdiction_name"
            ] = "CATHEDRAL CITY"
            df_from_dir.loc[
                (df_from_dir["jurisdiction_name"].str.upper() == "SAINT HELENA") &
                (df_from_dir["County_Name"].str.upper() == "NAPA"),
                "jurisdiction_name"
            ] = "ST. HELENA"
            # print(df_from_dir["jurisdiction_name"].unique())
            # print(df_from_dir["County_Name"].unique())
            
            # print(df_from_dir.columns)
            # for i, col in enumerate(df_from_dir.columns, 1):
            #     print(f"{i}. {col}")
            filtered_df_from_dir = df_from_dir[
                (df_from_dir["jurisdiction_name"].str.lower() == city.lower()) &
                (df_from_dir["County_Name"].str.lower() == county.lower())
            ]

            if len(filtered_df_from_dir) > 0:
                # print(len(filtered_df_from_dir))
                if df is None:
                    df = filtered_df_from_dir
                else:
                    df = gpd.concat([df, filtered_df_from_dir], ignore_index=True)

        if df is None or len(df) == 0:
            print("No data found for " + city + ", " + county)
            continue

        print(len(df))
        os.makedirs(output_dir, exist_ok=True)
        shapefile_dir_path = output_dir / "shapefile"
        df.to_file(shapefile_dir_path, driver='ESRI Shapefile')
        shutil.make_archive(shapefile_dir_path, 'zip', shapefile_dir_path)
        send2trash(shapefile_dir_path)
        print("shapefile created at " + str(output_dir.parent.stem))



        # hcd_shapefile_paths = glob.glob(path + "/output/hcd*/misc/shapefile.zip")
        # if len(hcd_shapefile_paths) == 0:
        #     print(path)


if __name__ == "__main__":
    create_shapefiles_from_geojson()