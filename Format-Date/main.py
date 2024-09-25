import pandas as pd

df = pd.read_csv('A')

df['B'] = pd.to_datetime(
    df['B'], format='C')

# df['B'] = df['B'].dt.strftime('E')

df.to_csv('D', index=False)

# Please refer to README to see what each variable is for