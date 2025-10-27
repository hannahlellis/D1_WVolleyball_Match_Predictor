    # Web Scrapping to Pull D1 Women's Volleyball Stats from NCAA Website
    # https://www.ncaa.com/robots.txt

def scrape_ncaa_volleyball_stats(category_name):
    # Import necessary libraries
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import time

    # Step 0: Which stats to pull?
    catergories = {'Hitting Percentage' : '45', 'Kills Per Set' : '46', 'Match W-L Pctg.' : '51',}

    # Step 1: Fetch the webpage
    url = "https://www.ncaa.com/stats/volleyball-women/d1/current/team/"
    url_params = ["", "/p2", "/p3", "/p4", "/p5", "/p6", "/p7"]

    data_df = pd.DataFrame()
    catergory = catergories['Hitting Percentage']

    for param in url_params:
        
        response = requests.get(url + catergory + param)
        html_content = response.text

        # Step 2: Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Step 3: Find relevant data
        stats_table = soup.find('div', class_='stats-wrap')

        data_rows = soup.find_all('td')

        # Step X: Extract relevant data
        data_values = [data.get_text(strip=True) for data in data_rows]

        # Data storage
        temp_data_df = pd.DataFrame([data_values[i:i+7] for i in range(0, len(data_values), 7)])
        data_df = pd.concat([data_df, temp_data_df], ignore_index=True)

        # Wait
        time.sleep(3)  # Be respectful to the server

    # Add header row
    header_row = soup.find_all('th')
    header_values = [header.get_text(strip=True) for header in header_row]
    data_df.columns = header_values

    # Return DataFrame
    return data_df