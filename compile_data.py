from web_scraping import scrape_ncaa_volleyball_stats
import pandas as pd

# Win-Loss Percentage is output. Select input categories to pull.
category_names = [
    'Hitting Percentage',
    'Kills Per Set',
    'Assists Per Set',
    'Blocks Per Set',
    'Opposing Hitting Pctg',
    'Match W-L Pctg.'
]

# Map long category names to short keys we will use in a dict
key_map = {
    'Hitting Percentage': 'hp',
    'Kills Per Set': 'kps',
    'Assists Per Set': 'aps',
    'Blocks Per Set': 'bps',
    'Opposing Hitting Pctg': 'ohp',
    'Match W-L Pctg.': 'wlp',
}

dataframes = {}
for category in category_names:
    print(f"Compile Category: {category}")
    dataframes[key_map[category]] = scrape_ncaa_volleyball_stats(category)

merge_order = ['hp', 'kps', 'aps', 'bps', 'ohp', 'wlp']
suffix_map = {'kps': '_KPS', 'aps': '_APS', 'bps': '_BPS', 'ohp': '_OHP', 'wlp': '_WLP'}

combined_data_df = dataframes[merge_order[0]]
for key in merge_order[1:]:
    combined_data_df = pd.merge(
        combined_data_df,
        dataframes[key],
        on='Team',
        suffixes=('', suffix_map.get(key, '')),
        how='inner',
    )

combined_data_df.to_csv('combined_data.csv', index=False)