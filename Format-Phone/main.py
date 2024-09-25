import pandas as pd
import re

df = pd.read_csv('A')

def clean_phone(phone):
    return re.sub(r'D', 'E', phone)

df['B'] = df['B'].apply(clean_phone)

df.to_csv('C', index=False)
