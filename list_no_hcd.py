import glob
from src.util.data_path import data_path

def list_no_hcd():

    paths = glob.glob(data_path("*", "*"))

    for path in paths:
        hcd_shapefile_paths = glob.glob(path + "/output/hcd*/misc/shapefile.zip")
        if len(hcd_shapefile_paths) == 0:
            print(path)


if __name__ == "__main__":
    list_no_hcd()