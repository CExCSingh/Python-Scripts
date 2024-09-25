# Format-Phone File

This script will read a CSV file and format a phone number field based on a regex provided

## Inputs:

- A: The path to the csv file you would like to re-format
- B: The field you would like to re-format
- C: The name of the file which will be generated with only the selected field updated
- D: The regex which will be matched
- E: What will replace what is matched by the regex
- - For example: D = ' x\d+' and E = ''
- - This will look for any number ending with ' X123' (can be any amount of numbers) and replace it with a '' (blank string)



