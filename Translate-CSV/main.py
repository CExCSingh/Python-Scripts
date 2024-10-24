import pandas as pd
from deep_translator import GoogleTranslator

def TranslateColumn(file_path, field_to_translate, field_to_filter, value_to_filter, language_to_translate_to, output_file_name):
    df = pd.read_csv(file_path)
    print("Read CSV file")
    
    translator = GoogleTranslator(target=language_to_translate_to)
    
    df[field_to_translate] = df.apply(
        lambda row: translator.translate(row[field_to_translate]) if pd.notna(row[field_to_translate]) and row[field_to_filter] == value_to_filter 
        else row[field_to_translate], axis=1)
    
    print("Translated file")
    
    df.to_csv(output_file_name, index=False)
    print(f"Created output file: {output_file_name}")
    
if __name__ == '__main__':
    file_path = './sys_translation1.csv'
    field_to_translate = 'value'
    field_to_filter = 'locale'
    value_to_filter = 'zh'
    language_to_translate_to = 'zh-CN'
    output_file_name = 'output1.csv'
    TranslateColumn(file_path, field_to_translate, field_to_filter, value_to_filter, language_to_translate_to, output_file_name)
