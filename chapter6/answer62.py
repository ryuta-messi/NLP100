import joblib
model = joblib.load('model.joblib')
top10_similar_to_United_States = model.most_similar('United_States',topn=10)

print(top10_similar_to_United_States)