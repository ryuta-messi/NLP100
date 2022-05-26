import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X_train = pd.read_table('train.feature.txt',header=None)
X_test = pd.read_table('test.feature.txt',header=None)
X_valid = pd.read_table('valid.feature.txt',header=None)
y_train = pd.read_table('train.txt',header=None)[1]
y_test = pd.read_table('test.txt',header=None)[1]
y_valid = pd.read_table('valid.txt',header=None)[1]


C_candidate = [0.01,0.1,1.0,10]
train_accuracy = []
test_accuracy = []
valid_accuracy = []

for c in C_candidate:
    model = LogisticRegression(random_state=0,C=c)
    model.fit(X_train,y_train)
    train_accuracy.append(accuracy_score(y_train,model.predict(X_train)))
    test_accuracy.append(accuracy_score(y_test,model.predict(X_test)))
    valid_accuracy.append(accuracy_score(y_valid,model.predict(X_valid)))
    


plt.plot(C_candidate,train_accuracy,label="train accuracy")
plt.plot(C_candidate,test_accuracy,label="test accuracy")
plt.plot(C_candidate,valid_accuracy,label="valid accuracy")

plt.legend()
plt.show()