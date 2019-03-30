#!usr/bin/python
import io
import jieba
import sys
import numpy as np
import pandas as pd
import wordcloud
from scipy.misc import imread
import matplotlib.pyplot as plt
from pylab import mpl
import seaborn as sns

#myfont = FontProperties(fname='/usr/share/fonts/chinese/simhei.ttf')
mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体

mpl.rcParams['font.family']='sans-serif'
mpl.rcParams['axes.unicode_minus']=False

f=io.open('./government2019.txt',encoding='utf-8')
content = f.read()
jieba.load_userdict('dict1.txt')
txt_cut = jieba.cut(content)
stop_list = pd.read_csv('./stop1.txt',engine='python',encoding='utf-8',names=['t'])['t'].tolist()
result2= [w for w in txt_cut if w not in stop_list and w.strip() != '']
#result3 = [w for w in txt_cut if w not in ['的','有','多','大','，','！','“','”','。','、','是','在','等','·','，','要',' ']]
#print('/'.join(txt_cut))

word_count = pd.Series(result2).value_counts().sort_values(ascending=False)[0:30]
fig = plt.figure(figsize=(15,8))
x = word_count.index.tolist()
y = word_count.values.tolist() 
sns.barplot(x, y, palette="BuPu_r")
plt.title('词频Top20')
plt.ylabel('count') 
sns.despine(bottom=True)
plt.savefig('./两会政府报告词频.png',dpi=400)
plt.show()

f.close()
