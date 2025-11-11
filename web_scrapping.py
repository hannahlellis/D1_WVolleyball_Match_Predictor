    # Web Scrapping to Pull D1 Women's Volleyball Stats from NCAA Website
    # https://www.ncaa.com/robots.txt


# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_ncaa_volleyball_stats(catergory_name):

    catergories = {
        'Hitting Percentage' : '45', 
        'Kills Per Set' : '46',
        'Assists Per Set' : '47',
        'Blocks Per Set' : '49',
        'Opposing Hitting Pctg' : '911', 
        'Match W-L Pctg.' : '51',
        }

    # Step 1: Fetch the webpage
    url_main = "https://www.ncaa.com/stats/volleyball-women/d1/current/team/"
    url_revisions = ["", "/p2", "/p3", "/p4", "/p5", "/p6", "/p7"]

    # Step 2: Scrape website for data from specified catergory
    catergory = catergories[catergory_name]
    data_df = pd.DataFrame()

    for url in url_revisions:
        
        response = requests.get(url_main + catergory + url)
        html_content = response.text

        # Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find relevant data
        stats_table = soup.find('div', class_='stats-wrap')
        data_rows = soup.find_all('td')
        header_row = soup.find_all('th')
    
        # Extract relevant data
        data_values = [data.get_text(strip=True) for data in data_rows]
        header_values = [header.get_text(strip=True) for header in header_row]

        # Store relevant data
        temp_data_df = pd.DataFrame([data_values[i:i+7] for i in range(0, len(data_values), len(header_values))])
        data_df = pd.concat([data_df, temp_data_df], ignore_index=True)
        data_df.columns = header_values
        # Wait
        time.sleep(5)  # Be respectful to the server

    # Return DataFrame
    return data_df