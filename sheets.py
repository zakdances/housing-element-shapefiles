# import gspread
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import pandas as pd

import gspread
from util.find_features import find_features
# from oauth2client.service_account import ServiceAccountCredentials

# Set pandas options to display the full DataFrame
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)  # Auto adjust width based on content
pd.set_option('display.max_colwidth', None)  # Display full content of columns

token_path = "token.json"

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly", 'https://spreadsheets.google.com/feeds']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1X691RBS_-0LlXX-bfAE9GXXu0P1OJnbERTqipn-C1jQ"
SAMPLE_RANGE_NAME = "Class Data!A1:E"

def up2():

    # credentials = Credentials.from_service_account_file(token_path, SCOPES)
    gc = gspread.service_account(filename=token_path)

    # gc = gspread.authorize(credentials)

    sh = gc.open_by_key(SAMPLE_SPREADSHEET_ID)  

    worksheet = sh.worksheet('ABAG')

    # cell_value = worksheet.cell("A1").value 

    dataframe = pd.DataFrame(worksheet.get_all_records())
    dataframe = dataframe.sort_values(by=['County', 'Municipality']).reset_index(drop=True)

    munis = dataframe[['County', 'Municipality']].values.tolist()
    
    features = find_features(munis)
    features = features.rename(columns={'Features_Count': 'APNs'})
    features = features.sort_values(by=['County', 'Municipality']).reset_index(drop=True)

    # print(features.values.tolist())
    # print(len(features))
    # print(len(dataframe))
    # return

    # Concatenate the DataFrames side by side
    # df_side_by_side = pd.concat([dataframe, features], axis=1, keys=['df1', 'df2'])

    # Display the result
    # print(df_side_by_side)
    # return

    # Display the mismatched rows
    # Merge with indicator to show where the rows come from
    merged = pd.merge(dataframe, features, on=['County', 'Municipality'], how='outer', indicator=True)

    # Mismatched rows (not in both DataFrames)
    mismatched_in_dataframe = merged[merged['_merge'] == 'left_only'].drop(columns='_merge')
    mismatched_in_features = merged[merged['_merge'] == 'right_only'].drop(columns='_merge')

    if len(mismatched_in_dataframe) > 0 or len(mismatched_in_features) > 0:
        # Display the mismatched rows
        print("Mismatched rows in dataframe:")
        print(mismatched_in_dataframe)

        print("\nMismatched rows in features:")
        print(mismatched_in_features)
        raise Exception("Mismatch found!")

    # county_match = set(dataframe['County']) == set(features['County'])
    # municipality_match = set(dataframe['Municipality']) == set(features['Municipality'])

    # if not county_match or not municipality_match:
    #     # To find mismatched rows (rows in dataframe but not in features and vice versa)
    #     county_mismatched_in_dataframe = dataframe[~dataframe['County'].isin(features['County'])]
    #     county_mismatched_in_features = features[~features['County'].isin(dataframe['County'])]

    #     municipality_mismatched_in_dataframe = dataframe[~dataframe['Municipality'].isin(features['Municipality'])]
    #     municipality_mismatched_in_features = features[~features['Municipality'].isin(dataframe['Municipality'])]

    #     # Output the mismatched rows
    #     print("Mismatched counties in dataframe:")
    #     print(county_mismatched_in_dataframe)

    #     print("\nMismatched counties in features:")
    #     print(county_mismatched_in_features)

    #     print("\nMismatched municipalities in dataframe:")
    #     print(municipality_mismatched_in_dataframe)

    #     print("\nMismatched municipalities in features:")
    #     print(municipality_mismatched_in_features)
    #     raise Exception("Mismatch found!")
    

    # df_merged = pd.merge(dataframe, features, on=['County', 'Municipality'], how='outer')
    dataframe['APNs'] = features['APNs']

    # print(len(features))
    # print(len(dataframe))
    # print(dataframe)

    worksheet.update([dataframe.columns.values.tolist()] + dataframe.values.tolist())

    # print(dataframe.values.tolist())
    # print(features)

def upload_dataframe_to_sheets(
        df=None, 
        spreadsheet_name=None, 
        sheet_name=None, 
        credentials_path=None):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        raise Exception("No valid credentials found")
        # if creds and creds.expired and creds.refresh_token:
        #     creds.refresh(Request())
        # else:
        #     flow = InstalledAppFlow.from_client_secrets_file(
        #         "credentials.json", SCOPES
        #     )
        #     creds = flow.run_local_server(port=0)
        # # Save the credentials for the next run
        # with open("token.json", "w") as token:
        #     token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return

        print("Name, Major:")
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print(f"{row[0]}, {row[4]}")

    except HttpError as err:
        print(err)

if __name__ == "__main__":
    # split_geojson("SB6A__pts_Join_3616231054980920121.geojson")
    # loop()
    # find_dupes()
    up2()