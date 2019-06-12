import pandas as pd
import os
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.parse
import urllib
import requests
from urllib.request import Request, urlopen

PATH = '/Users/rohan/Documents/Grad School/coursework/winter/ML & NLP/project_code/data/fin_data/reuters_new/'
path_files = (files for pth, dirs, files in os.walk(PATH))
FORMAT_PATH = PATH + '{}'
path_list = []
for i in path_files:
    for j in i:
        path_list.append(FORMAT_PATH.format(j))


path_list.remove('/Users/rohan/Documents/Grad School/coursework/winter/ML & NLP/project_code/data/'
                 'fin_data/reuters_new/.DS_Store')
path_list.remove('/Users/rohan/Documents/Grad School/coursework/winter/ML & NLP/project_code/data/'
                 'fin_data/reuters_new/read.py')

SEARCH_URL = 'http://api.duckduckgo.com/?q={}&format=json'

df_list = []
for i in path_list:
    df = pd.read_json(open(i, 'r', encoding='utf-8'), lines=True)
    df.drop_duplicates(subset=None, keep='first', inplace=False)
    for j in df['title']:
        temp_j = re.sub('[^A-Za-z0-9 ]*', '', j.lower())
        new_j = temp_j.replace(' ', '+')
        new_val = SEARCH_URL.format(new_j)
        print(new_val)
