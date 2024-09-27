import pandas as pd
import sys

def filterScript(file_path, column_name, filter_value, output_file_name):
    file = file_path
    df = pd.read_csv(file)
    filtered_df = df[df[column_name] == filter_value]
    filtered_df.to_csv(output_file_name, index=False)

if __name__ == '__main__':
    params = sys.argv
    if len(params) == 5:
        file_path = params[1]
        column_name = params[2]
        filter_value = params[3]
        output_file_name = params[4]
        filterScript(file_path, column_name, filter_value, output_file_name)
    else: 
        raise Exception("Incorrect number of arguments given. 4 arguments are required")

