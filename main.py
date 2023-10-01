"""
This is the main python file
"""

import pandas as pd
import json
import os
# Question 1
folder_path = 'data/massive'
dfs = []
for filename in os.listdir(folder_path):
    
    file_path = os.path.join(folder_path, filename)
    df = pd.read_json(file_path,orient='records',lines=True)
    dfs.append(df)

print(f'{len(dfs)} files have been converted')

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

# Question 2 (a)
en_train = dfs[10][dfs[10]['partition']=='train']
en_train.to_json('json/en_train.jsonl',orient='records',lines=True)

en_test = dfs[10][dfs[10]['partition']=='test']
en_test.to_json('json/en_test.jsonl',orient='records',lines=True)

en_dev = dfs[10][dfs[10]['partition']=='dev']
en_dev.to_json('json/en_dev.jsonl',orient='records',lines=True)


de_train = dfs[8][dfs[8]['partition']=='train']
de_train.to_json('json/de_train.jsonl',orient='records',lines=True)


