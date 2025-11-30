from web_scrapping import scrape_ncaa_volleyball_stats

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
data = data_hp + data_kps + data_aps + data_bps + data_ohp + data_wlp

print(data)

