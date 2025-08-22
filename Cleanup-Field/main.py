import pandas as pd

def cleanUpFile(fileName,outputFileName):
    df = pd.read_csv(fileName, dtype=str, sep='|', keep_default_na=False, quoting=1) 
    df = df.applymap(
        lambda x: x.replace('\n', ' ').replace('\r', ' ').strip() if isinstance(x, str) else x
    )    
    df.to_csv(outputFileName, index=False, sep='|', quoting=1)

if __name__ == "__main__":
    fileName = "input.csv"
    identifier = "\n"
    replacer = ""
    outputFileName = "output.csv"

    cleanUpFile(fileName, outputFileName)