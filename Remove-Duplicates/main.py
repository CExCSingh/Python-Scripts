import pandas as pd

df = pd.read_csv('A')

filtered_df = df.drop_duplicates(subset=['B'])

filtered_df.to_csv('C', index=False)
