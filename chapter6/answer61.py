model = joblib.load('model.joblib')
cosine_similarity = model.similarity('United_States','U.S.')

print(cosine_similarity)