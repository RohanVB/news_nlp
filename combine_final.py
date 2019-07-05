import pandas as pd
import os

data_path = '/Users/rohan/Documents/Grad School/coursework/winter/ML & NLP/project_code/data/results/' \
            'marketwatch_results.csv'
file_path = '/Users/rohan/Documents/Grad School/Coursework/Winter/ML & NLP/Project_Code/data/company_prices'
path_pth = ''.join([pth for pth, dirs, files in os.walk(file_path)])
path_files = [files for pth, dirs, files in os.walk(file_path)]

total_vals = [item for sublist in path_files for item in sublist]

reuters_df = pd.read_csv(data_path)

for i in total_vals:
    try:
        left = pd.DataFrame()
        ticker_list = []
        text_list = []
        headlines_list = []
        date_list = []

        for j, k, l, m in zip(reuters_df['Ticker'], reuters_df['text'], reuters_df['headlines'], reuters_df['date']):
            if j == i:
                ticker_list.append(j)
                text_list.append(k)
                headlines_list.append(l)
                date_list.append(m)

        left['ticker'] = ticker_list
        left['text'] = text_list
        left['timestamp'] = date_list
        left['headlines'] = headlines_list
        left = left.dropna()
        left = left.sort_values('timestamp')

        right = pd.read_csv(path_pth + '/' + i)  # timestamp, ticker, signal
        right = right.dropna()
        right = right.sort_values('timestamp')

        new_df = left.merge(right, on='ticker', how='inner')
        new_df = new_df.dropna()
        # new_df.to_csv('/Users/rohan/Documents/Grad School/coursework/winter/ML & NLP/'
        #               'project_code/data/results/marketwatch_task_test/' + i)
    except KeyError:
        print(i)
