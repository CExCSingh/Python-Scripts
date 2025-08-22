import pandas as pd

def updateField(fileName, delimiter, columns, outputFileName='output.csv'):
    df = pd.read_csv(fileName, delimiter=delimiter, dtype=str)

    for col in columns:
        if col in df.columns:
            df[col] = df[col].str.lower().replace({'true': 'yes', "false":"no"})
        else:
            print(f"Warning: Column '{col}' not found in file.")
    
    df.to_csv(outputFileName, index=False, sep=delimiter)

    print(f"Updated file saved to {outputFileName}")


if __name__ == "__main__":
    fileName = 'input.csv'
    delimiter ='|'
    columns=['primary_issue']
    updateField(fileName, delimiter, columns, "issue_20250702.csv")