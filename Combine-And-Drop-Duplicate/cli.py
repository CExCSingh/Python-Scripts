import pandas as pd
import sys

def combineAndDropDuplicate(file_one_path,file_two_path,field_array,output_file_name):

    file_one = pd.read_csv(file_one_path, keep_default_na=False, na_values=[''])

    file_two = pd.read_csv(file_two_path, keep_default_na=False, na_values=[''])

    combined_df = pd.concat([file_one, file_two])

    unique_df = combined_df[field_array].drop_duplicates()

    unique_df.to_csv(output_file_name, index=False)


if __name__ == '__main__':
    params = sys.argv
    if len(params) >= 5:
        file_one_path = params[1]
        file_two_path = params[2]
        output_file_name = params[3]
        fields_array = params[4:]
        combineAndDropDuplicate(file_one_path, file_two_path, fields_array, output_file_name)
    else:
        raise Exception('Incorrect number of parameters given. A minimum of 4 parameters are required')