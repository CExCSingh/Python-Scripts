import pandas as pd
import sys

def removeDuplicate(file_path, field, output_file_path):
    df = pd.read_csv(file_path)
    filtered_df = df.drop_duplicates(subset=[field])
    filtered_df.to_csv(output_file_path, index=False)

if __name__ == '__main__':
    params = sys.argv
    if len(params) == 4:
        file_path = params[1]
        field = params[2]
        output_file_path = params[3]
        removeDuplicate(file_path, field, output_file_path)
    else:
        raise Exception("Incorrect number of arguments given. 3 arguments are required")