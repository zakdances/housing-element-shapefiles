import pandas as pd
from pytablewriter import MarkdownTableWriter
from furl import furl
import glob
from urllib.parse import urlparse, urlunparse, quote, urlencode

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import gspread

token_path = "token.json"

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly", 'https://spreadsheets.google.com/feeds']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1X691RBS_-0LlXX-bfAE9GXXu0P1OJnbERTqipn-C1jQ"
SAMPLE_RANGE_NAME = "Class Data!A1:F"
repoUrl = "https://github.com/zakdances/housing-element-shapefiles/tree/main"

def data_path(county, municipality, as_url=False, parse_url=False):
    path = f"counties/{county}/cities/{municipality}"
    if as_url:
        path = f"{repoUrl}/{path}"
        if parse_url:
            path = furl(path).url
    return path


def insert_text_into_markdown(file_path, insert_text, insert_after_line):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Insert the new text after the specified line number
    lines.insert(insert_after_line, insert_text + "\n")

    # Write the modified content back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(lines)

def delete_line_range(file_path, start_line, end_line, empty_lines=0):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Remove the specified range (adjusting for zero-based index)
    new_lines = lines[:start_line - 1] + lines[end_line:]

    # Add the specified number of empty lines after the deleted range
    # new_lines.extend(["\n"] * empty_lines)

    # Write the updated content back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(new_lines)


def get_summary_line_range(file_path):
    start_line = None
    end_line = None

    with open(file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            if line.strip().startswith("## START Summary"):
                start_line = line_number
            elif line.strip().startswith("## END Summary"):
                end_line = line_number
                break  # Stop searching once the end is found

    if start_line is not None and end_line is not None:
        return (start_line, end_line)
    else:
        return None  # Return None if the range is incomplete

def gen():
    gc = gspread.service_account(filename=token_path)
    sh = gc.open_by_key(SAMPLE_SPREADSHEET_ID)  

    sacog_worksheet = sh.worksheet('SACOG')
    abag_worksheet = sh.worksheet('ABAG')
    scag_worksheet = sh.worksheet('SCAG')

    sacog_dataframe = pd.DataFrame(sacog_worksheet.get_all_records())
    abag_dataframe = pd.DataFrame(abag_worksheet.get_all_records())
    scag_dataframe = pd.DataFrame(scag_worksheet.get_all_records())

    sacog_dataframe['Link'] = abag_dataframe.apply(lambda row: f'[link]("{data_path(row['County'], row['Municipality'], True, True)}/output")', axis=1)
    abag_dataframe['Link'] = abag_dataframe.apply(lambda row: f'[link]("{data_path(row['County'], row['Municipality'], True, True)}/output")', axis=1)
    scag_dataframe['Link'] = abag_dataframe.apply(lambda row: f'[link]("{data_path(row['County'], row['Municipality'], True, True)}/output")', axis=1)

    # Create Markdown table writers
    sacog_writer = MarkdownTableWriter()
    abag_writer = MarkdownTableWriter()
    scag_writer = MarkdownTableWriter()

    # Set DataFrame values
    sacog_writer.from_dataframe(sacog_dataframe)
    abag_writer.from_dataframe(abag_dataframe)
    scag_writer.from_dataframe(scag_dataframe)

    file_path = "README.md"
    line_range = get_summary_line_range(file_path)
    adjusted_range = (line_range[0] + 1, line_range[1] - 1)


    delete_line_range(file_path, *adjusted_range)

    # Print the Markdown table
    table_string = "\n# ABAG\n" + abag_writer.dumps()
    table_string += "\n# SACOG\n" + sacog_writer.dumps()
    table_string += "\n# SCAG\n" + scag_writer.dumps()


    # print(table_string)
    
    # Insert the table into the README file
    insert_text_into_markdown(file_path, table_string, line_range[0] + 0)

if __name__ == "__main__":

    gen()