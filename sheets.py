import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

def upload_dataframe_to_sheets(df, spreadsheet_name, sheet_name, credentials_path):
    """
    Uploads a pandas DataFrame to a Google Sheet.

    Args:
        df (pd.DataFrame): The DataFrame to upload.
        spreadsheet_name (str): The name of the Google Sheet spreadsheet.
        sheet_name (str): The name of the sheet within the spreadsheet.
        credentials_path (str): The path to the Google Cloud service account credentials JSON file.
    """
    # Define the scope of permissions
    scope = [
        "https://www.googleapis.com/auth/spreadsheets.readonly",
    ]

    # Load credentials from the JSON file
    creds = Credentials.from_service_account_file(credentials_path, scopes=scope)

    # Authenticate with Google Sheets API
    client = gspread.authorize(creds)

    # Open the spreadsheet by name
    try:
        spreadsheet = client.open(spreadsheet_name)
    except gspread.exceptions.SpreadsheetNotFound:
        print(f"Spreadsheet '{spreadsheet_name}' not found.")
        return

    # Select the sheet by name
    try:
        sheet = spreadsheet.worksheet(sheet_name)
    except gspread.exceptions.WorksheetNotFound:
        print(f"Sheet '{sheet_name}' not found in spreadsheet '{spreadsheet_name}'.")
        return

    # Clear existing data in the sheet
    sheet.clear()

    # Get the list of values from the DataFrame
    data = [df.columns.tolist()] + df.values.tolist()

    # Update the sheet with the DataFrame data
    sheet.update(data)

    print(f"DataFrame successfully uploaded to '{sheet_name}' in '{spreadsheet_name}'.")

if __name__ == "__main__":
    # split_geojson("SB6A__pts_Join_3616231054980920121.geojson")
    # loop()
    # find_dupes()
    upload_dataframe_to_sheets()