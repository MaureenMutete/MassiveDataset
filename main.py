"""
This is the main python file
"""

import pandas as pd
import json
import os

# Replace 'folder_path' with the path to your folder containing JSONL files
folder_path = 'data/massive'

# Initialize an empty list to store DataFrames for each file
dfs = []



# Loop through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".jsonl"):
        # Construct the full path to the JSONL file
        file_path = os.path.join(folder_path, filename)

        # Initialize an empty list to store parsed JSON objects
        data_list = []

        try:
            # Read JSONL file line by line and parse each line as JSON
            with open(file_path, 'r', encoding='utf-8') as file:  # Specify the encoding here
                for line in file:
                    try:
                        json_obj = json.loads(line)
                        data_list.append(json_obj)
                    except json.JSONDecodeError as e:
                        print(f"Error parsing JSON in {file_path}: {e}")

            # Convert the list of JSON objects to a DataFrame
            if data_list:
                df = pd.DataFrame(data_list)

                # Append the DataFrame to the list of DataFrames
                dfs.append(df)
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")

# Combine all DataFrames into a single DataFrame
if dfs:
    final_df = pd.concat(dfs, ignore_index=True)
    print(f'Combined {len(dfs)} JSONL files into a single DataFrame.')
else:
    final_df = pd.DataFrame()

dataframes = []

for index in range(len(dfs)):
    for filename in os.listdir(folder_path):

        testdata = {
        'id': dfs[10]['id'],
        'en-utt': dfs[10]['utt'],
        f'{filename[:2]}-utt': dfs[index]['utt'],
        'en-annot_utt':dfs[10]['annot_utt'],
        f'{filename[:2]}-annot_utt':dfs[index]['annot_utt']
        }

        dframe = pd.DataFrame(testdata)
        dframe.to_excel(f"excel/en-{filename[:2]}.xlsx")



