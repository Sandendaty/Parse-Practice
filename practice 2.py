# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:55:22 2023

@author: 86133
"""

import requests
url="https://www.bitpush.news/covid19/"
html=requests.get(url).text
from lxml import etree
etree.HTMLParser(encoding='utf-8')
doc=etree.HTML(html)
reigon=doc.xpath('//*[@id="main"]/div[2]/div/div/div/div/div[1]/table/tbody/tr/td[1]/span/text()')
infected=[int(i.replace(',','')) for i in doc.xpath('//*[@id="main"]/div[2]/div/div/div/div/div[1]/table/tbody/tr/td[2]/text()')]
dead=[int(i.replace(',','')) for i in doc.xpath('//*[@id="main"]/div[2]/div/div/div/div/div[1]/table/tbody/tr/td[3]/text()')]
import pandas as pd
df=pd.DataFrame({'reigons':reigon,'infected':infected,'dead':dead})
df2=df.sort_values(by='infected',ascending=False).iloc[0:15]
import matplotlib
matplotlib.rcParams['font.family']='simHei'
import matplotlib.pyplot as plt
x,y=df2['reigons'].map(lambda x:'\n'.join(x)),df2['infected']
plt.bar(x,height=y,color=['red','orange','green','#1f77b4','#1f77b4','#1f77b4','#1f77b4','#1f77b4','#1f77b4','#1f77b4','#1f77b4','#1f77b4','#1f77b4','#1f77b4','#1f77b4'])
plt.xlabel('美国的地区')
plt.ylabel('确诊人数')
plt.title('美国的COVID-19疫情确诊人数排名前15的地区')
for i,j in zip(x,y):
    plt.text(i,j,j,ha='center',va='top',rotation=90,color='white')
plt.show()