# Remove-Duplicate File

This script will read a csv file and remove all duplicate values from the csv

## Inputs:

- file_path: The path to the csv file you would like to re-format
- field: Name of the column to check for duplicates
- output_file_path: The name of the file which will be generated

## This script will remove all duplicates of a value in a column, while keeping the first occurrence in the file
- This is the default behavior of the .drop_duplicates method

## CLI Tool
- The cli tool will take 3 arguments
    - The path to the file
    - The field to filter and check for duplicates
    - The name of the output file

### Example
```
python cli ./file.csv first_name output.csv
```