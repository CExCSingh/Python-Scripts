# Format-Phone File

This script will read a CSV file and format a phone number field based on a regex provided

## Inputs:

- file_path: The path to the csv file you would like to re-format
- field: The field you would like to re-format
- output_file_name: The name of the file which will be generated with only the selected field updated
- regex_pattern: The regex which will be matched
- replacer: What will replace what is matched by the regex
- - For example: D = ' x\d+' and E = ''
- - This will look for any number ending with ' X123' (can be any amount of numbers) and replace it with a '' (blank string)

## CLI Tool
- The CLI tool will take 5 arguments
    - The path to the file
    - The field to format
    - The name of the output file
    - The regex pattern to match 
        - Must be passed as a string
    - What to replace the matched data with
        - Must be passed as a string

### Example
```
python cli.py ./file.csv Phone output.csv ' x/d+' ''
```

