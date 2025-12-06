#TEST
import pandas as pd

data_kps = pd.read_csv('data_kps.csv')
data_kps.drop(columns=['Rank'], inplace=True)
data_kps.rename(columns={'Per Set':'KPS'}, inplace=True)
data_aps = pd.read_csv('data_aps.csv')
data_aps.drop(columns=['Rank'], inplace=True)
data_aps.rename(columns={'Per Set':'APS'}, inplace=True)

# Merge row-wise (union of columns)
merged_df = pd.concat([data_kps, data_aps], ignore_index=True, sort=False)

combined_data_df = pd.merge(
    data_kps, data_aps, 
    on='Team',
    suffixes=('_KPS', '_APS')
)
combined_data_df.to_csv('combineddata.csv', index=False)

print(data_kps.columns)
print(data_kps.head())
print(data_aps.columns)
print(f"Merged DF: {merged_df.columns}")
print(f"Combined DF: {combined_data_df.head()}")

print(f"DataFrame size {data_kps.shape[0]} rows and {data_kps.shape[1]} columns")
print(f"DataFrame size {data_aps.shape[0]} rows and {data_aps.shape[1]} columns")
print(f"Combined size {combined_data_df.shape[0]} rows and {combined_data_df.shape[1]} columns")