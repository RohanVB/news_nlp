import pandas as pd
import os
import re
import shutil
import pickle

"""
PATH FOR INPUT NEWS
"""
reuters_path = '/Users/rohan/Documents/Grad School/Coursework/Winter/ML & NLP/Project_Code/data/reuters'
bloomberg_path = '/Users/rohan/Documents/Grad School/Coursework/Winter/ML & NLP/Project_Code/data/bloomberg'

"""
GET THE COMPLETE PATH AND FILES
"""
path_pth = [pth for pth, dirs, files in os.walk(bloomberg_path)]
path_files = [files for pth, dirs, files in os.walk(bloomberg_path)]
company_list_500 = pd.read_csv('/Users/rohan/Documents/Grad School/Coursework/Winter'
                               '/ML & NLP/Project_Code/data/constituents.csv').dropna(axis=0, how='any')
company_list = company_list_500['Symbol']

all_files = []
all_paths = []
all_paths_files = []
for i, n in zip(path_pth, path_files):
    for j in n:
        all_files.append(j)
        all_paths.append(i)
        all_paths_files.append(i + '/' + j)

total_vals = []
for n in all_files:
    p = re.compile('(.*)_')
    if p.findall(n):
        total_vals.append(p.findall(n))
    else:
        total_vals.append(' ')
total_vals = [item for sublist in total_vals for item in sublist]

for i, j, k in zip(total_vals, all_files, all_paths):
    try:
        os.rename(k + '/' + j, k + '/' + i)
    except:
        print('ERROR')
