import os
import glob
import json
from src.util.data_path import data_path
from pathlib import Path

def check_folders(base_path="counties"):
    sources_with_missing_output = []
    path = data_path("*", "*")

    for municipality in glob.glob(path):

        municipality = Path(municipality)

        input_path = municipality / "input"
        output_path = municipality / "output"
        meta_path = municipality / "meta.json"

        # Check if the input path exists and the output path does not exist

        if not input_path.exists():
            continue

        for item in input_path.iterdir():
            huh = output_path / item.stem / "misc" / "shapefile.zip"

            # If shapefile.zip exists or invalid file type, skip
            if huh.exists() or item.name == ".DS_Store":
                continue

            # Check if the meta file confirms that there is no apns in this source
            if meta_path.exists():
                with open(meta_path, "r") as f:
                    meta = json.load(f)

                obj = meta.get(item.name) or meta.get(item.stem)

                if obj and (obj.get("no_apns") or obj.get("no_apns") or obj.get("skip")):
                    if obj.get("skip"):
                        print(f"Skipping {item.name} in {municipality.name} because of meta.json")
                    continue

            sources_with_missing_output.append(huh)

        # if os.path.isdir(input_path) and not os.path.isdir(output_path):
        #     sources_with_missing_output.append(municipality)
    
    for source in sources_with_missing_output:
        print(source)

    # for county in glob.glob(f"{base_path}/*"):
    #     city_path = f"{county}/cities"
    #     if not os.path.isdir(city_path):
    #         continue
        
    #     for municipality in glob.glob(f"{city_path}/*"):
    #         input_path = f"{municipality}/input"
    #         output_path = f"{municipality}/output"
            
    #         if os.path.isdir(input_path) and not os.path.isdir(output_path):
    #             missing_folders.append(output_path)
    
    # if missing_folders:
    #     print("Missing output folders:")
    #     for folder in missing_folders:
    #         print(folder)
    # else:
    #     print("All input folders have corresponding output folders.")

if __name__ == "__main__":
    check_folders()