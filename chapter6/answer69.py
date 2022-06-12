from cv2 import countNonZero
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from gensim.models import KeyedVectors
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans

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

tsne = TSNE().fit_transform(X)
# plt.scatter(tsne[:,0],tsne[:,1])
# plt.annotate(countryName,xy=(tsne[:,0],tsne[:,1]))
# plt.show()
km = KMeans(n_clusters=5,random_state=0)
y_km = km.fit_predict(X)

fig, ax = plt.subplots(figsize=(16, 8))
cmap = plt.get_cmap('Dark2')
for i in range(tsne.shape[0]):
    cval = cmap(y_km[i]/4)
    ax.scatter(tsne[i][0], tsne[i][1], marker='.', color=cval)
    ax.annotate(countryName[i], xy=(tsne[i][0], tsne[i][1]), color=cval)
plt.show()