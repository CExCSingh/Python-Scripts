# Combine-And-Drop-Duplicate Script

This script will combine two csv's provided and generate a new csv file with no duplicate values

## Inputs:

- A: The path to csv file one
- B: The path to csv file two
- C: An array which includes the fields you want to include in the combined csv, and will drop duplicates based on those fields
- D: The name of the file which will be generated

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