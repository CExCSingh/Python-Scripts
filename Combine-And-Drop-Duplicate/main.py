import pandas as pd

file_one = pd.read_csv('A', keep_default_na=False, na_values=[''])
file_two = pd.read_csv('B', keep_default_na=False, na_values=[''])

combined_df = pd.concat([file_one, file_two])

unique_df = combined_df['C'].drop_duplicates()

unique_df.to_csv('D', index=False)
