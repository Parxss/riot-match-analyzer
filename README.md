# Riot Games Match Data Analyzer

A command-line application built in Python that interacts with the Riot Games API to extract, analyze, and export League of Legends player data. 

## Features
* **Multi-Endpoint Routing:** Converts Riot IDs to PUUIDs using the `Account-V1` endpoint before querying the `Match-V5` endpoint.
* **JSON Parsing:** Navigates complex, nested API payloads to extract specific participant data out of 10-player rosters.
* **Interactive CLI:** Includes a user-friendly menu for analyzing single matches or bulk-averaging recent game statistics.
* **Automated Reporting:** Generates clean `.csv` spreadsheet exports of player match history for further database use.

## Technologies Used
* **Python 3:** Core application logic and control flow.
* **Requests:** Handling HTTP GET requests and API authentication.
* **JSON & CSV:** Parsing raw web data and structuring it into standardized spreadsheet formats.

## How to Run Locally
1. Clone this repository to your local machine.
2. Generate a Developer API Key from the [Riot Developer Portal](https://developer.riotgames.com/).
3. Open `app.py` (or your main script file) and replace `"YOUR_API_KEY_HERE"` with your active token.
4. Run the script in your terminal using:
   ```bash
   python3 app.py
