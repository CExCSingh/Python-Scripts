import pandas as pd

file_name = 'A'

df = pd.read_csv(file_name)

filtered_df = df[df['B'] == 'C']

filtered_df.to_csv('D', index=False)
