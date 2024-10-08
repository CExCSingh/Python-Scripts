import pandas as pd

def combineAndDropDuplicate(file_one_path,file_two_path,field_array,output_file_name):

    file_one = pd.read_csv(file_one_path, keep_default_na=False, na_values=[''])

    file_two = pd.read_csv(file_two_path, keep_default_na=False, na_values=[''])

    combined_df = pd.concat([file_one, file_two])

    unique_df = combined_df[field_array].drop_duplicates()

    unique_df.to_csv(output_file_name, index=False)


if __name__ == '__main__':
    file_one_path = './one.csv'
    file_two_path = './two.csv'
    fields_array = ['first','last','age']
    output_file_name = 'output.csv'
    combineAndDropDuplicate(file_one_path, file_two_path, fields_array, output_file_name)