# Lethal Company Bee Seed Tracker
## What It Does
- Monitors your VLog files (from the modded game).
- Detects the most recent bee seed and how many times it has appeared.
- Sends this information to a Google Sheet if anything changes.
## Requirements
### Python Environment
- Make sure you have **Python 3.10+** installed.
- Install required packages with:
  ```bash
  pip install -r requirements.txt
    ```
## Setup Instructions
### 1. Install Required Mods for Lethal Company
You’ll need these mods installed via Thunderstore:
- **Loadstone** by AdiBTW  
  https://thunderstore.io/c/lethal-company/p/AdiBTW/Loadstone/
- **VLog** by HQHQTeam  
  https://thunderstore.io/c/lethal-company/p/HQHQTeam/VLog/
- **High Quota Fixes** by Chboo1  
  https://thunderstore.io/c/lethal-company/p/Chboo1/High_Quota_Fixes/
### 2. Set Up Google Sheets API
Follow this video to set up your Google API service account:  
https://www.youtube.com/watch?v=zCEJurLGFRk

Steps:
- Create a service account.
- Enable the Google Sheets API.
- Download the `credentials.json` file.
- Place `credentials.json` in the same folder as the script.
- Share your target Google Sheet with the service account's email.
### 3. Update Your Spreadsheet Info
Open `google_sheets.py` and **replace the spreadsheet ID**:
```python
SPREADSHEET_ID = 'your-google-sheet-id-here'
```
Once setup is complete, just run:
```bash
python main.py
```
## File Locations
By default, the VLog directory it watches is:
```
C:/Users/<YourUserName>/AppData/LocalLow/ZeekerssRBLX/Lethal Company/VLogs
```
This is automatically handled in the program, so you don’t need to change it unless your game is installed in a non-standard location.

## How It Works

- Python reads text files line-by-line.
- The `main.py` script looks for lines like:
```
Log: Setting bee random seed: 12345678
```
- It grabs the most recent seed and counts how many times it appears.
- Then it subtracts from the seed value to compute a special ID.
- Only if the seed or count has changed since last check, it updates the Google Sheet.

## Resources
- Google Sheet Script (by hackercat)
https://github.com/hackercat27/lethal-rng/blob/main/script.js
- 1A3 v70 Code Diffs
https://1a3.uk/games/lethal-company/diffs/v70_1?tab=1
- My High Quota Spreadsheet
https://docs.google.com/spreadsheets/d/131JmTANkfvGDPAzufmVrGQLgAHXUl8_vx26qhszFoS0/