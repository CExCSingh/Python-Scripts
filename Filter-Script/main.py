import pandas as pd

def filterScript(file_path, column_name, filter_value, output_file_name):
    file = file_path
    df = pd.read_csv(file)
    filtered_df = df[df[column_name] == filter_value]
    filtered_df.to_csv(output_file_name, index=False)

if __name__ == '__main__':
    file_path = ''
    column_name = ''
    filter_value = ''
    output_file_name = ''
    filterScript(file_path, column_name, filter_value, output_file_name)