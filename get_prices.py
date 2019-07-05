import pandas as pd
import requests
import io
import os

company_list_500 = pd.read_csv('/Users/rohan/Documents/Grad School/Coursework/Winter'
                               '/ML & NLP/Project_Code/data/get_prices.csv').dropna(axis=0, how='any')

file_path = '/Users/rohan/Documents/Grad School/Coursework/Winter/ML & NLP/Project_Code/data/company_prices'
path_files = [files for pth, dirs, files in os.walk(file_path)]

total_vals = [item for sublist in path_files for item in sublist]

if '.DS' in total_vals:
    total_vals.remove('.DS_Store')

companies = list(set(company_list_500['Symbol']))

final_list = []
for i in companies:
    if i not in total_vals:
        final_list.append(i)

print(len(total_vals))
# """
# api-key1: 7XG6B9AIG3BWQTD9
# api-key2: XV58BB1TT7YPZ3SH
# api-key3: DN4GVEGU96EQ7CXG
# api-key4: 85UAVS4J40XLIZ71
# api-key5: 6TWN0IZ85EQTW84O
# """
# for name in final_list:
#     try:
#         scrape_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + str(name) + '&outputsize=full&apikey=6TWN0IZ85EQTW84O&datatype=csv'
#         price = requests.get(scrape_url).content
#         df = pd.read_csv(io.StringIO(price.decode('utf-8')))
#         df = df.loc[:,'timestamp':'open']   # only use open price
#         df['ticker'] = name     # create one row
#         mask = (df['timestamp'] >= '2006-10-20') & (df['timestamp'] <= '2013-11-26')    # set time series
#         print(df.loc[mask])
#         df = df.loc[mask]
#         # df.index = range(len(df['timestamp']))      # reindex dataframe
#         diff = []
#         status = []
#         signal = []
#         # print(len(df['timestamp']))
#         for i in range(len(df['timestamp'])-1):
#             diff.append(df.iloc[i]['open'] - df.iloc[i+1]['open'])
#             status.append(diff[i]/ df.iloc[i]['open'])
#             if status[i] > 0.0055:    # set increase rate higher than 0.55% =1
#                 signal.append(1)
#             elif status[i] < -0.005:    # set increase rate lower than 0.5% = 0
#                 signal.append(0)
#             else:
#                 signal.append('stay')
#         # diff.append(1)
#         # status.append(0)
#         signal.append(1)
#         print('shape of signal and diff is: ', len(signal), len(diff))
#         # df.insert(4,'diff',diff)
#         df.insert(3,'signal',signal)
#         print(df)
#         df = df[df.signal!='stay']    ## get only 1 and 0, get rid of stay.
#         df.index = range(len(df['timestamp']))      # reindex dataframe
#         # print(df.shape)
#         df.to_csv('/Users/rohan/documents/Grad School/Coursework/winter/ML & NLP/project_code/data/company_prices/' + name)      # save every company price into a file.
#     except:
#         df.to_csv('/Users/rohan/documents/Grad School/Coursework/winter/ML & NLP/project_code/data/error_companies/' + name)
#         continue
