import pandas as pd
from datetime import datetime

import re

bloomberg_df = pd.read_csv('/Users/rohan/Documents/Grad School/coursework'
                           '/winter/ML & NLP/project_code/data/results/bloomberg.csv')

reuters_df = pd.read_csv('/Users/rohan/Documents/Grad School/coursework/'
                         'winter/ML & NLP/project_code/data/results/reuters.csv')


def headlines_fix(filename):
    my_list = []
    for i in filename:
        my_list.append(str(i).replace('--', ''))
    bloomberg_df['headlines'] = my_list
    print(bloomberg_df)

def datetime_fix(filename):
    my_list = []
    for i in filename:
        match = re.findall(r'\d{4}-\d{2}-\d{2}', str(i))
        if match:
            for matches in match:
                my_list.append(matches)
        else:
            my_list.append('')
    bloomberg_df['date'] = my_list


headlines_fix(bloomberg_df['headlines'])
datetime_fix(bloomberg_df['date'])

bloomberg_df.to_csv('/Users/rohan/Documents/Grad School/coursework/winter/ML & NLP/project_code/'
                    'data/results/preprocessed_bloomberg.csv')
