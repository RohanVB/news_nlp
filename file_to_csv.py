import pandas as pd
import os
import re
import shutil
import pickle

"""
PATH FOR INPUT NEWS
"""
reuters_path = '/Users/rohan/Documents/Grad School/Coursework/Winter/ML & NLP/Project_Code/data/reuters_results'
bloomberg_path = '/Users/rohan/Documents/Grad School/Coursework/Winter/ML & NLP/Project_Code/data/bloomberg_results'

"""
GET THE COMPLETE PATH AND FILES
"""

path_pth = [pth for pth, dirs, files in os.walk(bloomberg_path)]
path_files = [files for pth, dirs, files in os.walk(bloomberg_path)]

all_files = []
all_paths = []
all_paths_files = []

for i, n in zip(path_pth, path_files):
    for j in n:
        all_files.append(j)
        all_paths.append(i)
        all_paths_files.append(i + '/' + j)

date_list = []
headlines_list = []
text_list = []

all_paths_files = [x for x in all_paths_files if not '.DS' in x]
all_paths = [x for x in all_paths if not '.DS' in x]

df = pd.DataFrame()
ticker_list = []

for i in all_paths:
    ticker_list.append(os.path.basename(os.path.normpath(i)))
df['Ticker'] = ticker_list

for i in all_paths_files:
    try:
        with open(i, encoding='utf-8') as f:
            f.seek(0)
            lines = f.readlines()
            lines = [line.rstrip('\n') for line in lines]
            if '' not in lines[2:3]:
                date_list.append(''.join(lines[2:3]))
                headlines_list.append(''.join(lines[0:1]))
                text_list.append(''.join(lines[4:]))  # need to remove everything after 'To contact the editor responsible'
            else:
                date_list.append(''.join(lines[5:6]))
                headlines_list.append(''.join(lines[1:2]))
                text_list.append(''.join(lines[8:]))
    except UnicodeDecodeError:
        print('Unicode Error')


df['headlines'] = headlines_list
df['date'] = date_list
df['text'] = text_list

print(df)
# df.to_csv('/Users/rohan/Documents/Grad School/coursework/winter/ML & NLP/project_code/data/results/bloomberg.csv')
