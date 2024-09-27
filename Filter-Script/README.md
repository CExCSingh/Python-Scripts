# Filter-Script File

This script will read a csv file and only keep records which contain a specific value for a column selected

## Inputs:

- file_path: The path to the csv file you would like to re-format
- column_name: Name of the column 
- filter_value: Exact value to filter
- output_file_name: The name of the file which will be generated with only records that match filter_value in column column_name

## CLI Tool
- The CLI tool will take 4 arguments
    - Path to the file
    - The column to be filtered
    - The value to filter
    - The name of the output field

```
python cli.py ./fileName.csv first_name charanvir output.csv
```