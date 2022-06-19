from itertools import count
import pandas as pd
import numpy as np
from gensim.models import KeyedVectors
from sklearn.cluster import KMeans

df = pd.read_csv('chapter6/CountryNames.csv')

countries =df['country names'].values
# print(countries)

# model = KeyedVectors.load_word2vec_format('chapter6/GoogleNews-vectors-negative300.bin.gz',binary=True)
# model.save('chapter6/word2vec.model')
model = KeyedVectors.load('chapter6/word2vec.model')
print(type(model))


countryVec = []
countryName = []
#print(list(model.key_to_index.keys())[:10])  
## model.vocab is no longer availavle in gendim version 4.0.0
for c in countries:
    if c in model.key_to_index:
        countryVec.append(model[c])
        countryName.append(c)


print(countryName)

X = np.array(countryVec)
km = KMeans(n_clusters=5,random_state=0)
y_km = km.fit_predict(X)
print(y_km)