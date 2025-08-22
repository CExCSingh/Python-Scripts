import pandas as pd

def extractColumn(fileName, delimiter, columns, outputMethod, outputFileName = 'output.csv'):
    try:
        df = pd.read_csv(fileName, sep=delimiter, usecols=columns)
        if outputMethod == "print":
            print(df)
        elif outputMethod == "save":
            df.to_csv(outputFileName, index=False)
            print(f"Saved file to {outputFileName}")
    except FileNotFoundError:
        print(f"Error: File {fileName} not found")
    except ValueError as e: 
        print(f"Error: {e}")

if __name__ == '__main__':
    fileName = 'party.csv'
    delimiter = '|'
    columns = ['party_type', 'case_id']
    outputMethod = "print"
    extractColumn(fileName, delimiter, columns, outputMethod)
