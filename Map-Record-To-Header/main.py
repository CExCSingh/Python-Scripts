import csv
import json
import os


def csv_to_json(input_csv_path, output_json_path=None):
    if output_json_path is None:
        base = os.path.splitext(input_csv_path)[0]
        output_json_path = f"{base}.json"

    data = []

    with open(input_csv_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)

        for row in reader:
            if len(row) == len(headers):
                record = dict(zip(headers, row))
                data.append(record)
            else:
                print(f"Skipping row with mismatched columns: {row}")

    with open(output_json_path, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=2)

    print(f"JSON written to {output_json_path}")


if __name__ == "__main__":
    fileName = 'test.csv'
    csv_to_json(fileName)
