import numpy as np
from gensim.models import KeyedVectors
import joblib



model = joblib.load('chapter6/model.joblib')
# model = KeyedVectors.load_word2vec_format('chapter6/GoogleNews-vectors-negative300.bin.gz',binary=True)
result = model.most_similar(positive=['Spain','Athens'],negative=['Madrid'])[0] #Spain + Athens - Madrid


print(result)
# for i in range(10):
#     print(result[i])

