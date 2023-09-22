import requests
from bs4 import BeautifulSoup
import csv


URL = "https://www.multihousingnews.com/developer-seals-construction-debt-for-luxury-project/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}  # A common user-agent to bypass basic user-agent filtering

response = requests.get(URL, headers=HEADERS)

if response.status_code == 200:  # Check if the request was successful
    soup = BeautifulSoup(response.content, 'html.parser')

    # save paragraphs
    paragraphs = [paragraph.get_text() for paragraph in soup.find_all('p')]

     # Saving data to CSV
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Paragraphs"])  # Writing header
        for paragraph in paragraphs:
            writer.writerow([paragraph])

    print("Data saved to output.csv")

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
