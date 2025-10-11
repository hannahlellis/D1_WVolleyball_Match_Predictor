# Web Scrapping to Enable D1 Women's Volleyball Match Predictor
# https://www.ncaa.com/robots.txt

# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage
url = "https://www.ncaa.com/stats/volleyball-women/d1/current/team/45"
response = requests.get(url)
html_content = response.text

# Step 2: Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Find relevant data
stats_table = soup.find('div', class_='stats-wrap')
header_row = soup.find_all('th')
data_rows = soup.find_all('td')

# Step X: Extract relevant data
header_values = [header.get_text(strip=True) for header in header_row]
data_values = [data.get_text(strip=True) for data in data_rows]
print("Headers:", header_values)
print("Data Values:", data_values)

# Data storage

