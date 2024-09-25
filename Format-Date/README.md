# Format-Date File

This script will read a CSV file and format a date field to whatever format you enter.

## Inputs:

- A: The path to the csv file you would like to re-format
- B: The field you would like to re-format
- C: The format the field is currently in
- - Example: '%m/%d/%Y'
- - This will look for values with the following format mm/dd/yyyy
- D: The name of the file which will be generated with only the selected field updated
- E: The format you want to re-format the date to

## Note
### The pandas library will automatically re-format the date field to 'ISO 8601 format (YYYY-MM-DD)'
### I have included a line (8) which is currently commented out
#### It will allow you to choose the formatting 