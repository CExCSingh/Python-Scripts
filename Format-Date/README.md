# Format-Date File

This script will read a CSV file and format a date field to whatever format you enter.

## Inputs:

- file_path: The path to the csv file you would like to re-format
- field: The field you would like to re-format
- current_format: The format the field is currently in
- - Example: '%m/%d/%Y'
- - This will look for values with the following format mm/dd/yyyy
- output_file_name: The name of the file which will be generated with only the selected field updated
- desired_format (optional): The format you want to re-format the date to
- - desired_format will by default be an empty string. If a value is passed in the function call, it will refactor that field to follow the format entered

## Note
### The pandas library will automatically re-format the date field to 'ISO 8601 format (YYYY-MM-DD)'
### I have included a line (8) within an if conditional
#### It will allow you to choose the formatting 

## CLI Tool

The tool can take either 4 arguments or 5
    - Path to the file
    - Field to format
    - Current format of the field to format
        - Must be passed as a string ''
    - Name of the output file
    - (Optional) The desired format (will override the default formatting)
        - Must be passed as a string

### 4 Arguments
```
python cli.py ./file.csv Date_Of_Birth '%m/%d/%Y' output.csv
```

### 5 Arguments
```
python cli.py ./file.csv Date_Of_Birth '%m/%d/%Y' output.csv '%d %B %Y'
```