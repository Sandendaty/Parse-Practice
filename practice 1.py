# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 10:49:53 2023

@author: 86133
"""

import requests
url="https://www.bitpush.news/covid19/"
html=requests.get(url).text
from lxml import etree
etree.HTMLParser(encoding='utf-8')
doc=etree.HTML(html)
country=doc.xpath('//*[@id="main"]/div[1]/div/div/div/div/div[1]/table/tbody/tr/td[1]/span/text()')
infected=[int(i.replace(',','')) for i in doc.xpath('//*[@id="main"]/div[1]/div/div/div/div/div[1]/table/tbody/tr/td[2]/text()')]
dead=[int(i.replace(',','')) for i in doc.xpath('//*[@id="main"]/div[1]/div/div/div/div/div[1]/table/tbody/tr/td[3]/text()')]
import pandas as pd
df=pd.DataFrame({'地区':country,'确诊':infected,'死亡':dead})
df.to_csv('content.csv',index=False,header=False)
df2=df.sort_values(by='死亡',ascending=False).iloc[1:11]
import matplotlib
matplotlib.rcParams['font.family']='simHei'
import matplotlib.pyplot as plt
x,y=df2.iloc[:,0],df2.iloc[:,2]
plt.bar(x,height=y,color=['red','orange','green','#1f77b4','#1f77b4','#1f77b4','#1f77b4','#1f77b4','#1f77b4','#1f77b4'])
plt.xlabel('国家')
plt.ylabel('死亡人数')
plt.title('COVID-19疫情死亡人数排名前10的国家')
for i,j in zip(x,y):
    plt.text(i,j,j,ha='center',va='bottom')
plt.show()