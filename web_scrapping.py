# Web Scrapping to Enable D1 Women's Volleyball Match Predictor
# https://www.ncaa.com/robots.txt

# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Web scrapping of url
headers = {"User-Agent": "Mozilla/5.0"}  # Respectful header

# Step 1: Fetch the webpage
url = "https://www.ncaa.com/stats/volleyball-women/d1/current/team/45"
response = requests.get(url)

# Check that the request was successful
if response.status_code == 200:
    html_content = response.text

    # Step 2: Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Step 3: Extract specific elements
    # Example: Get all links
    links = soup.find_all('a')
    for link in links:
        print(link.get('href'))  # Print href attributes

    # Example: Get text of a specific CSS class
    headings = soup.find_all('h2', class_='title')
    for heading in headings:
        print(heading.get_text())
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Data extraction and cleaning


# Data storage

