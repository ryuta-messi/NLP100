import pandas as pd
import joblib
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt




X_train = pd.read_table('train.feature.txt',header=None)
X_test = pd.read_table('test.feature.txt',header=None)
y_train = pd.read_table('train.txt',header=None)[1]
y_test = pd.read_table('test.txt',header=None)[1]

model = joblib.load('model.joblib')

print(f'train confusion matrix: \n {confusion_matrix(y_train,model.predict(X_train))}')
print(f'test confusion matrix: \n {confusion_matrix(y_test,model.predict(X_test))}')

sns.heatmap(confusion_matrix(y_train,model.predict(X_train)),annot=True,cmap='Oranges')
plt.show()
sns.heatmap(confusion_matrix(y_test,model.predict(X_test)),annot=True,cmap='Oranges')
plt.show()
## revise about confusion_matrix 