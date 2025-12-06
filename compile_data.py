from web_scrapping import scrape_ncaa_volleyball_stats
import pandas as pd

# Win-Loss Percentage is output. Select input catergories to pull.
catergory_names = [
    'Hitting Percentage',
    'Kills Per Set', 
    'Assists Per Set', 
    'Blocks Per Set',
    'Opposing Hitting Pctg',
    'Match W-L Pctg.'
    ]

for catergory in catergory_names:
    print(f"Compile Category: {catergory}")
    temp_data = scrape_ncaa_volleyball_stats(catergory)
  
    if catergory == 'Hitting Percentage':
        data_hp = temp_data
    elif catergory == 'Kills Per Set':
        data_kps = temp_data
    elif catergory == 'Assists Per Set':
        data_aps = temp_data
    elif catergory == 'Blocks Per Set':
        data_bps = temp_data
    elif catergory == 'Opposing Hitting Pctg':
        data_ohp = temp_data
    elif catergory == 'Match W-L Pctg.':
        data_wlp = temp_data

# Combine input(s) and output into single DataFrame for model training
combined_data_df = data_hp
combined_data_df = pd.merge(combined_data_df, data_kps, on='Team', suffixes=('', '_KPS'))
combined_data_df = pd.merge(combined_data_df, data_aps, on='Team', suffixes=('', '_APS'))
combined_data_df = pd.merge(combined_data_df, data_bps, on='Team', suffixes=('', '_BPS'))
combined_data_df = pd.merge(combined_data_df, data_ohp, on='Team', suffixes=('', '_OHP'))
combined_data_df = pd.merge(combined_data_df, data_wlp, on='Team', suffixes=('', '_WLP'))

combined_data_df.to_csv('combined_data.csv', index=False)
