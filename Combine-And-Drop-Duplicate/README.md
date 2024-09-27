# Combine-And-Drop-Duplicate Script

This script will combine two csv's provided and generate a new csv file with no duplicate values

## Inputs:

- file_one_path: The path to csv file one
- file_two_path: The path to csv file two
- field_array: An array which includes the fields you want to include in the combined csv, and will drop duplicates based on those fields
- output_file_name: The name of the file which will be generated

## Examples:

- unique_df = combined_df[['Case #','Case Type]].drop_duplicates()

### File One:
Case #	Case Type   Issue Type
101 	A           One
102	    B           Two
101	    A           Three
103	    C           Four

### File Two:
Case #	Case Type   Party Type
101 	A           Reporter
102	    B           Witness
101	    A           Other
103	    C           Other

### Combined File (Pre duplicate drop):
Case #	Case Type   
101 	A           
102	    B           
101	    A         
103	    C       

### Final File (Duplicates drop):
Case #	Case Type   
101 	A           
102	    B           
103	    C    

## CLI Tool
- The CLI tool takes a minimum of 5 arguments
    - The path to the first file
    - The path to the second file
    - The name of the output file
    - A list of fields to include in the array of fields which will be filtered when combining and dropping duplicates

### Example of CLI tool 
```
python cli.py ./one.csv ./two.csv output.csv first last age
```
This will combine the two files and create output.csv with combined records that has no duplicates looking at the three (first, last, age) fields given

```
python cli.py ./one.csv ./two.csv output.csv first last
```
This will only take two fields (first, last) into account when determining which duplicates to drop