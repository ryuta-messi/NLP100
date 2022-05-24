import joblib

model = joblib.load('model.joblib')
vocabulary_  = joblib.load('vocabulary_.joblib')
coefs = model.coef_

for c in coefs[0]:
    print(c)
    # d = dict(zip(vocabulary_,c))
    # print(d.items())
    # d_top = sorted(d.items(),key=lambda x:abs(x[1]),reverse=True)[0]
    # print(d_top)