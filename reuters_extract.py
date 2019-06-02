import pandas as pd
import os
import re
import shutil
from difflib import SequenceMatcher
import pickle

"""
PATH FOR INPUT NEWS
"""
reuters_path = '/Users/rohan/Documents/Grad School/Coursework/Winter/ML & NLP/Project_Code/data/reuters'
bloomberg_path = '/Users/rohan/Documents/Grad School/Coursework/Winter/ML & NLP/Project_Code/data/bloomberg'

"""
GET THE COMPLETE PATH AND FILES
"""
path_pth = [pth for pth, dirs, files in os.walk(reuters_path)]
path_files = [files for pth, dirs, files in os.walk(reuters_path)]

all_files = []
all_paths = []
for i, n in zip(path_pth, path_files):
    for j in n:
        all_paths.append(i)
        all_files.append(i + '/' + j)

all_paths_short = all_paths[:100]
try:
    all_files.remove('/Users/rohan/Documents/Grad School/Coursework/Winter/ML & NLP/Project_Code/data/reuters/.DS_Store')
    all_paths_short = all_paths[1:101]
    all_paths = all_paths[1:]
except:
    print('no .DS_Store')
all_files_short = all_files[:100]

"""
GET THE FILE COMPANY NAMES AS THEY EXIST WITHIN THE FILE NAMES
"""

total_vals = []
for n in all_files:
    p = re.compile('us-(.*)-id')
    if p.findall(n):
        total_vals.append(p.findall(n))
    else:
        total_vals.append('-')

file_names = [item.replace('-', ' ') for sublist in total_vals for item in sublist]
file_names_short = file_names[:100]

"""
COMBINED NASDAQ + S&P 500 COMPANY LIST
"""

company_list_500 = pd.read_csv('/Users/rohan/Documents/Grad School/Coursework/Winter'
                               '/ML & NLP/Project_Code/data/constituents.csv').dropna(axis=0, how='any')

company_list = company_list_500['Value']
company_list = [x.lower() for x in company_list]

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

threshold = 0.95
result_list = []


for x in file_names:
    new_x = str(x).lower()
    new_x = re.sub('[^A-Za-z]+', ' ', new_x)
    first_list = []
    for i in new_x.split():
        for y in company_list:
            if similar(i, y) > threshold:
                first_list.append(y)
                print(y, i)
            else:
                first_list.append('')
    result_list.append(first_list)


with open('datafile_reuters.pkl', 'wb') as f:
    print('pickle dumping...')
    pickle.dump(result_list, f)

with open('datafile_reuters.pkl', 'rb') as f:
    newlist = pickle.load(f)

df_new = pd.DataFrame()
df_i = []
df_j = []
df_k = []

print('begin appending...')
for new_name, new_file, new_path in zip(newlist, all_files, all_paths):
    for i in set(new_name):
        if i != '':
            df_i.append(i)
        else:
            df_i.append('')
        df_j.append(new_file)
        df_k.append(new_path)
df_new['Keyword'] = df_i
df_new['File'] = df_j
df_new['Path'] = df_k
df_new['Symbol'] = df_new['Keyword'].map(dict(zip(company_list, company_list_500['Symbol'])))
df_new['Symbol'].fillna('none', inplace=True)

print('begin file renaming...')
for original_path, (count, new_name), path_val in zip(df_new['File'], enumerate(df_new['Symbol']), df_new['Path']):
    try:
        if new_name != 'none':
            # print(path_val + '/{}'.format(new_name), original_path)
            shutil.copy(original_path, path_val + '/{}_{}'.format(new_name, count))

        else:
            print('this one is none.')
            # shutil.move(original_path, path_val + '/{}'.format(new_name))
    except:
        print('fail', original_path, path_val, new_name) # error because it already gets turned into `none`

# todo: If company name exists as file name, then create a directory by company name and put all matching company names in there.
