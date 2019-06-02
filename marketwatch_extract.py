import pandas as pd
import os
import re
from difflib import SequenceMatcher
import itertools
import shutil
import numpy as np
import pickle
import collections

"""
PATH FOR INPUT NEWS
"""
news_path = '/Users/rohan/documents/Grad School/coursework/Winter/ML & NLP/project_code/data/fin_data' \
            '/marketwatch_new.csv'

df = pd.read_csv(news_path).drop_duplicates(subset=['title'], keep='first')

"""
COMBINED NASDAQ + S&P 500 COMPANY LIST
"""
# entire_company_list = pd.read_csv('/Users/rohan/Documents/Grad School/Coursework/Winter'
#                                   '/ML & NLP/Project_Code/data/entire_company_list.csv')
company_list_500 = pd.read_csv('/Users/rohan/Documents/Grad School/Coursework/Winter'
                               '/ML & NLP/Project_Code/data/constituents.csv').dropna(axis=0, how='any')

company_list = company_list_500['Value']
company_list = [x.lower() for x in company_list]
# def similar(a, b):
#     return SequenceMatcher(None, a, b).ratio()
#
#
# threshold = 0.95
# result_list = []
#
#
# for x in df['title']:
#     new_x = str(x).lower()
#     new_x = re.sub('[^A-Za-z]+', ' ', new_x)
#     first_list = []
#     for i in new_x.split():
#         for y in company_list:
#             if similar(i, y) > threshold:
#                 first_list.append(y)
#                 print(y, i)
#             else:
#                 first_list.append('')
#     result_list.append(first_list)
#
# with open('datafile.pkl', 'wb') as f:
#     pickle.dump(result_list, f)

with open('datafile.pkl', 'rb') as f:
    newlist = pickle.load(f)

df_new = pd.DataFrame()
df_j = []
df_k = []
df_l = []
df_m = []
df_n = []

for i, k, l, m, n in zip(newlist, df['title'], df['date'], df['article'], df['abstract']):
    for j in i:
        if j != '':
            df_j.append(j)
            df_k.append(k)
            df_l.append(l)
            df_m.append(m)
            df_n.append(n)
df_new['Keyword'] = df_j
df_new['Title'] = df_k
df_new['Date'] = df_l
df_new['Article'] = df_m
df_new['Abstract'] = df_n

new_val = (zip(company_list, company_list_500['Symbol']))
df_new['Symbol'] = df_new['Keyword'].map(dict(zip(company_list, company_list_500['Symbol'])))
# df_new.to_csv('/Users/rohan/documents/Grad School/coursework/Summer_Project/marketwatch_results.csv')
