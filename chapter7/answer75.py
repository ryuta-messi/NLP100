import joblib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import torch 
from torch import nn,optim



X_train = joblib.load('chapter7/X_train.joblib')
y_train = joblib.load('chapter7/y_train.joblib')

X_train = torch.from_numpy(X_train.astype(np.float32)).clone()
y_train = torch.from_numpy(y_train.astype(np.int64)).clone()


X_valid = joblib.load('chapter7/X_valid.joblib')
y_valid = joblib.load('chapter7/y_valid.joblib')

X_valid = torch.from_numpy(X_valid.astype(np.float32)).clone()
y_valid = torch.from_numpy(y_valid.astype(np.int64)).clone()


X_test = joblib.load('chapter7/X_test.joblib')
y_test = joblib.load('chapter7/y_test.joblib')

X_test = torch.from_numpy(X_test.astype(np.float32)).clone()
y_test = torch.from_numpy(y_test.astype(np.int64)).clone()

# print(X_train.size())

X = X_train[0:4]
y = y_train[0:4]

# print(X.size())
net = nn.Linear(X.size()[1],4)
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(),lr=0.01)

train_loss = []
valid_loss = []
train_accuracy = []
valid_accuracy = []



for epoc in range(100):
    optimizer.zero_grad()
    y_pred = net(X)
    loss = loss_fn(y_pred,y)
    loss.backward()
    optimizer.step()
    
    train_loss.append(loss)
    valid_loss.append(loss_fn(net(X_valid),y_valid))
    
    _,y_pred_train = torch.max(net(X),axis=1)
    train_accuracy.append((y_pred_train == y).sum().item() / len(y))
    _,y_pred_valid = torch.max(net(X_valid),axis=1)
    valid_accuracy.append((y_pred_valid == y_valid).sum().item()/len(y_valid))



plt.plot([item.item() for item in train_loss],label="train-loss")
plt.plot([item.item() for item in valid_loss],label='valid-loss')
plt.legend()
plt.show()

plt.plot(train_accuracy,label="train-accuracy")
plt.plot(valid_accuracy,label="valid-accuracy")
plt.legend()
plt.show()


# print(net.state_dict()['weight'])