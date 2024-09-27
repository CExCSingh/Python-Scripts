import pandas as pd
import re

def formatPhone(file_path, field, output_file_name, regex_pattern, replacer):        
    df = pd.read_csv(file_path)
    def clean_phone(phone):
        return re.sub(regex_pattern, replacer, str(phone))
    df[field] = df[field].apply(clean_phone)
    df.to_csv(output_file_name, index=False)

if __name__ == '__main__':
    file_path = ''
    field = ''
    output_file_name = ''
    regex_pattern = ''
    replacer = ''
    formatPhone(file_path, field, output_file_name, regex_pattern, replacer)