import pandas as pd
import sys

def formatDate(file_path, field, current_format, output_file_name, desired_format=''):

    df = pd.read_csv(file_path)
    df[field] = pd.to_datetime(
        df[field], format=current_format)
    if desired_format != '':
        df[field] = df[field].dt.strftime(desired_format)

    df.to_csv(output_file_name, index=False)

if __name__ == '__main__':
    params = sys.argv
    if len(params) == 5:
        file_path = params[1]
        field = params[2]
        current_format = params[3]
        output_file_name = params[4]
        desired_format = ''
        formatDate(file_path, field, current_format, output_file_name, desired_format)
    elif len(params) == 6:
        file_path = params[1]
        field = params[2]
        current_format = params[3]
        output_file_name = params[4]
        desired_format = params[5]
        formatDate(file_path, field, current_format, output_file_name, desired_format)
    else:
        raise Exception("Incorrect number of arguments passed. Pass 4 arguments to format field to ISO 8601 format (YYYY-MM-DD), or pass an additional 5th argument to format to a desired format.")
