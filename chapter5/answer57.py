import joblib

model = joblib.load('model.joblib')
vocabulary_  = joblib.load('vocabulary_.joblib')
coefs = model.coef_


print(len(coefs[0]))  #coefs [[b],[e],[t],[m]] それぞれのカテゴリーに寄与した単語の特徴量の重みが[b],[e],[t],[m]に格納されている
print(len(vocabulary_))
for c in coefs:
    d = dict(zip(vocabulary_,c)) #{単語:重み,.....}
    d_top = sorted(d.items(),key=lambda x:abs(x[1]),reverse=True)[:5]
    print(d_top)
    d_bottom = sorted(d.items(),key=lambda x:abs(x[1]),reverse=False)[:5]
    print(d_bottom)