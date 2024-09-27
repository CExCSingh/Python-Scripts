import pandas as pd
import sys
import re

def formatPhone(file_path, field, output_file_name, regex_pattern, replacer):        
    df = pd.read_csv(file_path)
    def clean_phone(phone):
        return re.sub(regex_pattern, replacer, str(phone))
    df[field] = df[field].apply(clean_phone)
    df.to_csv(output_file_name, index=False)

if __name__ == '__main__':
    params = sys.argv
    if len(params) == 6:
        file_path = params[1]
        field = params[2]
        output_file_name = params[3]
        regex_pattern = params[4]
        replacer = params[5]
        formatPhone(file_path, field, output_file_name, regex_pattern, replacer)
    else:
        raise Exception("Incorrect number of arguments given. 5 arguments are required")