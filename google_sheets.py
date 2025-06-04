from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load credentials
SERVICE_ACCOUNT_FILE = 'credentials.json' # ADD YOUR CREDENTIALS FILE
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Create service
service = build('sheets', 'v4', credentials=creds)

# Your spreadsheet ID and target cell
SPREADSHEET_ID = '131JmTANkfvGDPAzufmVrGQLgAHXUl8_vx26qhszFoS0' # REPLACE WITH YOUR SPREADSHEET ID
RANGE = "'Bee Calculator'!B3:C3"

def update_sheet(var_1, var_2):
    # Prepare request body
    body = {
        'values': [[var_1, var_2]]
    }

    # Call the Sheets API
    result = service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE,
     valueInputOption='RAW',
        body=body
    ).execute()