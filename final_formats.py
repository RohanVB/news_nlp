import pandas as pd
import os
import re
import shutil
import pickle

"""
PATH FOR INPUT NEWS
"""
reuters_path = '/Users/rohan/Documents/Grad School/Coursework/Winter/ML & NLP/Project_Code/data/results/reuters_task'
bloomberg_path = '/Users/rohan/Documents/Grad School/Coursework/Winter/' \
                 'ML & NLP/Project_Code/data/results/bloomberg_task'

"""
GET THE COMPLETE PATH AND FILES
"""

# path_pth = [pth for pth, dirs, files in os.walk(reuters_path)]
# path_files = [files for pth, dirs, files in os.walk(reuters_path)]
#
# all_files = []
# all_paths = []
# all_paths_files = []
#
# for i, n in zip(path_pth, path_files):
#     for j in n:
#         all_files.append(j)
#         all_paths.append(i)
#         all_paths_files.append(i + '/' + j)
#
# all_paths_files = [x for x in all_paths_files if not '.DS' in x]
# all_paths = [x for x in all_paths if not '.DS' in x]
#
#
# all_vals = []
# for i in all_paths_files:
#     val = pd.read_csv(i)
#     all_vals.append(val)
#
# result = pd.concat(all_vals, sort=True)
# print(result)
#
# lbl = result['signal'].value_counts()
# print(lbl)
#
# csv_df = pd.DataFrame()
#
# csv_df['timestamp'] = result['timestamp']
# csv_df['signal'] = result['signal']
# # csv_df['headlines'] = result['headlines']
# csv_df['ticker'] = result['ticker_x']
# csv_df['text'] = result['text']
#
# csv_df.sort_values(by=['timestamp'], inplace=True, ascending=True)
#
# print(csv_df)
# csv_df.to_csv('/Users/rohan/Documents/Grad School/Coursework/Winter/'
#               'ML & NLP/Project_Code/data/results/reuters_labeled.csv')

df1 = pd.read_csv('/Users/rohan/Documents/Grad School/Coursework/Winter/'
                  'ML & NLP/Project_Code/data/results/bloomberg_labeled.csv')
df2 = pd.read_csv('/Users/rohan/Documents/Grad School/Coursework/Winter/'
                  'ML & NLP/Project_Code/data/results/bloomberg_labeled.csv')

result = pd.concat([df1, df2], sort=True)
result.sort_values(by=['timestamp'], inplace=True, ascending=True)
result = result.drop(['Unnamed: 0'], axis=1)

result['signal'] = [int(i) for i in result['signal']]

result = result[['timestamp', 'signal', 'ticker', 'text']]

train_result = result[:13500]
test_result = result[13500:15044].drop(['signal', 'ticker'], axis=1)
dev_result = result[15044:].drop(['signal', 'ticker'], axis=1)

print(train_result)

train_result.to_csv('/Users/rohan/Documents/Grad School/Coursework/Winter/'
                    'ML & NLP/Project_Code/data/results/train.tsv', sep='\t', index=False, header=False)
test_result.to_csv('/Users/rohan/Documents/Grad School/Coursework/Winter/'
                   'ML & NLP/Project_Code/data/results/test.tsv', sep='\t', index=False, header=True)
dev_result.to_csv('/Users/rohan/Documents/Grad School/Coursework/Winter/'
                  'ML & NLP/Project_Code/data/results/dev.tsv', sep='\t', index=False, header=True)
