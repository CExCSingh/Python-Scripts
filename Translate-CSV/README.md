# Translate CSV

This script will read a csv file and translate a selected field to a supported language, based on a common value for a selected filter field

## Inputs

- file_path: The path to csv file
- field_to_translate: The column in the CSV you wish to get translated
- field_to_filter: Which field to use to filter records
- value_to_filter: Value to be filtered 
- language_to_translate_to: Language Code to selected the language to translate the selected field to
- output_file_name: Name and path of the output field

## This script's primary usage is for translating the value in sys_translation to allow additional languages to be imported to systems

## CLI Tool
- The cli tool can take a number of arguments
    - To use the tool, please use the following format for your command
        ```
        python cli.py <file_path> <field_to_translate> <field_to_filter> <value_to_filter> <language_to_translate_to> <output_file_name>
        ```
    - To get a list of all supported languages and their respective language codes
        ```
        python cli.py showAll
        ```
    - To check if a specific language is supported
        ```
        python cli.py show <language>
        ```

