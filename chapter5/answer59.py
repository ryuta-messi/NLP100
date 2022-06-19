from matplotlib.cbook import maxdict
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

X_train = pd.read_table('train.feature.txt',header=None)
X_test = pd.read_table('test.feature.txt',header=None)
X_valid = pd.read_table('valid.feature.txt',header=None)
y_train = pd.read_table('train.txt',header=None)[1]
y_test = pd.read_table('test.txt',header=None)[1]
y_valid = pd.read_table('valid.txt',header=None)[1]

test_accuracy = []

C_candidate = [0.01,0.1,1.0,10]

for c in C_candidate:
    model = LogisticRegression(random_state=0,C=c)
    model.fit(X_train,y_train)
    test_accuracy.append(accuracy_score(y_test,model.predict(X_test)))
    

max_depth_candidate = [2,4,8,16]

for depth in max_depth_candidate:
    tree_model = RandomForestClassifier(max_depth=depth,random_state=0)
    tree_model.fit(X_train,y_train)
    test_accuracy.append(accuracy_score(y_test,tree_model.predict(X_test)))
    
bestModelIndex = test_accuracy.index(max(test_accuracy))

if bestModelIndex < 4:
    bestAlgorithm = 'LogisticRegression'
    bestParam = C_candidate[bestModelIndex]
else:
    bestAlgorithm = 'RandomForestClassifier'
    bestParam = max_depth_candidate[bestModelIndex-4]
    
print(bestAlgorithm,bestParam)
    
    