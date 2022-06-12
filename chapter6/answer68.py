from itertools import count
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from gensim.models import KeyedVectors
from scipy.cluster.hierarchy import linkage,dendrogram


df = pd.read_csv('chapter6/CountryNames.csv')

countries =df['country names'].values
# print(countries)

# model = KeyedVectors.load_word2vec_format('chapter6/GoogleNews-vectors-negative300.bin.gz',binary=True)
# model.save('chapter6/word2vec.model')
model = KeyedVectors.load('chapter6/word2vec.model')

countryVec = []
countryName = []
#print(list(model.key_to_index.keys())[:10])  
## model.vocab is no longer availavle in gendim version 4.0.0
for c in countries:
    if c in model.key_to_index:
        countryVec.append(model[c])
        countryName.append(c)



X = np.array(countryVec)

linkage_result = linkage(X,method='ward',metric='euclidean')#Ward法による階層型クラスタリング
plt.figure(num=None, figsize=(16,8))
dendrogram(linkage_result,labels=countryName)#クラスタリング結果をデンドログラムとして可視化
plt.show()