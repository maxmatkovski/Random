import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time

# Ensure the directory exists, create it if not
os.makedirs('RE-Data', exist_ok=True)

urls = ["https://www.multihousingnews.com/vanrock-buys-north-carolina-community/",

"https://www.multihousingnews.com/eagle-property-pays-49m-for-orlando-apartments/"]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


# Empty DataFrame to store the bold texts
all_data = pd.DataFrame()

for url_index, url in enumerate(urls, start=1):
    try:
        response = requests.get(url, headers=HEADERS)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            bold_texts = [bold_text.get_text() for bold_text in soup.find_all(['b', 'strong'])]

            # Creating a DataFrame for this page
            df = pd.DataFrame([bold_texts], index=[url_index])

            # Appending this page's data to the main DataFrame
            all_data = pd.concat([all_data, df])

            print(f"Data collected from {url}")

        else:
            print(f"Failed to retrieve the webpage {url}. Status code: {response.status_code}")

        # Delay to prevent overwhelming the server
        time.sleep(2)  # 2 second delay, adjust as necessary

    except Exception as e:
        print(f"An error occurred: {e}")

# Saving data to an Excel file
all_data.to_excel('RE-Data/output.xlsx', sheet_name='Sheet1', index_label='Index')

print("Data saved to RE-Data/output.xlsx")