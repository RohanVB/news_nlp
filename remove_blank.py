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

path_pth = [pth for pth, dirs, files in os.walk(reuters_path)]
path_files = [files for pth, dirs, files in os.walk(reuters_path)]

all_files = []
all_paths = []
all_paths_files = []
for i, n in zip(path_pth, path_files):
    for j in n:
        all_files.append(j)
        all_paths.append(i)
        all_paths_files.append(i + '/' + j)

for i, j in zip(all_files, all_paths_files):
    if i == ' ':
        # print(j)
        os.remove(j)
