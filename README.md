# 🏐 **NCAA D1 Volleyball Win-Loss Record Predictions**

## Description: 
This project uses the below team stats to predict a team's Win-Loss Percentage.

## Dependencies:
- requests
- beautifulsoup4
- pandas
- time

## Team Stats
- Hitting Percentage
- Kills Per Set
- Assists Per Set
- Blocks Per Set
- Opposing Hitting Percentage

## Project Structure
- `web_scraping.py` - Scrapes the NCAA website for team statistics
- `compile_data.py` - Compiles scraped data into a single pandas DataFrame
- `predictions.py` - Trains the model and visualizes results

## Usage
- To scrape data and save CSV files: `python compile_data.py`
- To train and visualize model results: `python predictions.py`

Expected output:
- `combined_data.csv` (compiled dataset)
- `feature_importances.png` and `pred_vs_actual.png` (plots)