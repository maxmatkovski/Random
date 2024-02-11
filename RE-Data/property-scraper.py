from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import os
import time

# Ensure the directory exists, create it if not
os.makedirs('RE-Data', exist_ok=True)

# Start the WebDriver
driver = webdriver.Chrome(executable_path='C:/Users/maxma/Downloads/chromedriver_win32/chromedriver.exe')

# Navigate to the page
driver.get("https://www.multihousingnews.com/market-rate/")

# Find all the article links
article_links = [element.get_attribute('href') for element in driver.find_elements(By.CSS_SELECTOR, "a.article-title")]

# Quit the driver as it's no longer needed
driver.quit()

# Empty DataFrame to store the bold texts
all_data = pd.DataFrame()

for url_index, url in enumerate(article_links, start=1):
    try:
        response = requests.get(url)

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

# Saving data to a CSV file
all_data.to_csv('RE-Data/output.csv', index_label='Index')

print("Data saved to RE-Data/output.csv")