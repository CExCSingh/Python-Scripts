import pandas as pd

def removeDuplicate(file_path, field, output_file_path):        
    df = pd.read_csv(file_path)
    filtered_df = df.drop_duplicates(subset=[field])
    filtered_df.to_csv(output_file_path, index=False)

if __name__ == '__main__':
    file_path = ''
    field = ''
    output_file_path = ''
    removeDuplicate(file_path, field, output_file_path)