# Remove-Duplicate File

This script will read a csv file and remove all duplicate values from the csv

## Inputs:

- A: The path to the csv file you would like to re-format
- B: Name of the column to check for duplicates
- C: The name of the file which will be generated

## This script will remove all duplicates of a value in a column, while keeping the first occurrence in the file
- This is the default behavior of the .drop_duplicates method
- To keep the last value, you can pass this as a second argument to the .drop_duplicates method:  keep='last'

