import pandas as pd
from deep_translator import GoogleTranslator
import sys

def TranslateColumn(file_path, field_to_translate, field_to_filter, value_to_filter, language_to_translate_to, output_file_name):
    df = pd.read_csv(file_path)
    print("Read CSV file")
    
    translator = GoogleTranslator(target=language_to_translate_to)
    
    def translate_text(text, filter_value):
        if pd.notna(text):
            if len(text) > 5000:
                print(f"Skipping translation for text in row where {field_to_translate} is too long (over 5000 characters).")
                return text 
            return translator.translate(text)
        return text
    
    df[field_to_translate] = df.apply(
        lambda row: translate_text(row[field_to_translate], row[field_to_filter]) if row[field_to_filter] == value_to_filter 
        else row[field_to_translate], axis=1)
    
    print("Translated file")
    
    df.to_csv(output_file_name, index=False)
    print(f"Created output file: {output_file_name}")

def showAllLanguageCode():
    languageCodes = GoogleTranslator().get_supported_languages(as_dict=True)
    print(languageCodes)
    for language, code in languageCodes.items():
        print(f"Language: {language} - Language Code: {code}")

def showSpecificLanguageCode(language):
    languageCodes = GoogleTranslator().get_supported_languages(as_dict=True)
    if language in languageCodes:
        print(f"Language: {language} - Language Code: {languageCodes[language]}")
    else:
        print("This language is not supported")
    
if __name__ == '__main__':
    params = sys.argv
    if len(params) == 7:
        file_path = params[1]
        field_to_translate = params[2]
        field_to_filter = params[3]
        value_to_filter = params[4]
        language_to_translate_to = params[5]
        output_file_name = params[6]
        TranslateColumn(file_path, field_to_translate, field_to_filter, value_to_filter, language_to_translate_to, output_file_name)
    elif len(params) == 1:
        print("Run the command with --help to get a list of commands and arguments required")
    elif len(params) == 2 and params[1] == '--help':
        helpMessage = """
        To Translate the File, please run the command as such
        python cli.py <file_path> <field_to_translate> <field_to_filter> <value_to_filter> <language_to_translate_to> <output_file_name>
        <language_to_translate_to> is a language code used by Deep Translator to recognize which language to translate the selected field to

        To get a list of all language codes, please run the following command:
        python cli.py showAll

        To get a language code for a specified language, please run the following command:
        python cli.py show <language>
        """
        print("*****************")
        print(helpMessage)
        print("*****************")
    elif len(params) == 2 and params[1] == 'showAll':
        showAllLanguageCode()
    elif len(params) == 3 and params[1] == "show":
        showSpecificLanguageCode(params[2].lower())
    else:
        raise Exception("Incorrect number of arguments passed. Pass 6 arguments to run the script")


