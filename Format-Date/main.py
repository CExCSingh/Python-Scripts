import pandas as pd

def formatDate(file_path, field, current_format, output_file_name, desired_format=''):

    df = pd.read_csv(file_path)
    df[field] = pd.to_datetime(
        df[field], format=current_format)
    if desired_format != '':
        df[field] = df[field].dt.strftime(desired_format)

    df.to_csv(output_file_name, index=False)

if __name__ == '__main__':
    file_path = ''
    field = ''
    current_format = ''
    output_file_name = ''
    desired_format = ''
    formatDate(file_path, field, current_format, output_file_name, desired_format)