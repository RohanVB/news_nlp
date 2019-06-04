import pandas as pd
from datetime import datetime

import re

bloomberg_df = pd.read_csv('/Users/rohan/Documents/Grad School/coursework'
                           '/winter/ML & NLP/project_code/data/results/bloomberg.csv')

reuters_df = pd.read_csv('/Users/rohan/Documents/Grad School/coursework/'
                         'winter/ML & NLP/project_code/data/results/reuters.csv')

DATAFRAME = reuters_df

def headlines_fix(filename):
    my_list = []
    for i in filename:
        my_list.append(str(i).replace('--', ''))
    DATAFRAME['headlines'] = my_list

def datetime_fix_bloomberg(filename):
    my_list = []
    for i in filename:
        match = re.findall(r'\d{4}-\d{2}-\d{2}', str(i))
        if match:
            for matches in match:
                my_list.append(matches)
        else:
            my_list.append('')
    DATAFRAME['date'] = my_list

def datetime_fix_reuters(filename):
    my_list = []
    for i in filename:
        match = re.findall(r'(\D{3} \d{1,2}, \d{4})', str(i))
        # match = datetime.strptime(match.(), '%B %d, %Y')
        if match:
            for matches in match:
                match_value = datetime.strptime(matches, '%b %d, %Y').strftime('%Y-%m-%d')
                my_list.append(match_value)
        else:
            my_list.append('')
    DATAFRAME['date'] = my_list

headlines_fix(DATAFRAME['headlines'])
# datetime_fix_bloomberg(DATAFRAME['date'])
datetime_fix_reuters(DATAFRAME['date'])

print(DATAFRAME)

DATAFRAME.to_csv('/Users/rohan/Documents/Grad School/coursework/winter/ML & NLP/project_code/'
                 'data/results/preprocessed_reuters.csv')
