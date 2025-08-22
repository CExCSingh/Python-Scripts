import math
import pandas as pd

def splitFile (inputFile, separator, outputPrefix, splitAmount):
    df = pd.read_csv(
    inputFile,
    delimiter=separator,
    quoting=3,
    dtype=str,
    engine="python",      
    on_bad_lines="skip"    
)

    total_rows = len(df)

    rows_per_split = math.ceil(total_rows / splitAmount)

    for i in range(splitAmount):
        start = i * rows_per_split
        end = start + rows_per_split
        chunk = df.iloc[start:end]

        output_file = f"{outputPrefix}{i+1}.csv"
        chunk.to_csv(output_file, index=False)
        print(f"Saved {output_file} with {len(chunk)} rows")


if __name__ == "__main__":
    splitFile("case_20250605.csv", "|", "case", 6)