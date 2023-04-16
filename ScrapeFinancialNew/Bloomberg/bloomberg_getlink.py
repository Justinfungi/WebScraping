import requests
from bs4 import BeautifulSoup as bs
from lxml import etree
from urllib import request
import re
import pandas as pd
import numpy as np



def localfile(CorpName):
    link = f"{CorpName}.html"
    with open(link,'r') as html_file:
        article = html_file.read()
    return article

def onlinefile(CorpName):
    link = f"https://www.bloomberg.com/search?query={CorpName}"
    article = requests.get(link)
    return article

if local = True:
    s =localfile(filename)
else:
    s =onlinefile(filename)

s = bs(local,'lxml')
link = s.find_all("a",attrs={"class":"thumbnailWrapper__23c201ad78"})
target = []
for i in link:
    target.append(i["href"])
    print(i["href"])



pd.DataFrame(target).to_csv(f'{filename}.csv')
