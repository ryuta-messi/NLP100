import joblib
import numpy as np
from tqdm import tqdm
import torch
from torch.utils.data import TensorDataset,DataLoader
from torch import nn,optim
import matplotlib.pyplot as plt




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

X = X_train
y = y_train
if torch.cuda.is_available():
    X = X.to('cuda')
    y = y.to('cuda')

dataset = TensorDataset(X,y)

net = nn.Linear(X.size()[1],4)
loss_fn = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(),lr=0.01)

batchSize = [16]


for batchsize in batchSize:
    loader = DataLoader(dataset,batch_size=batchsize,shuffle=True)
    
    train_loss = []
    valid_loss = []
    train_accuracy = []
    valid_accuracy = []
    
    for epoc in tqdm(range(100)):
        train_running_loss = 0.0
        valid_running_loss = 0.0
        
        for xx,yy in loader:
            y_pred = net(xx)
            loss = loss_fn(y_pred,yy)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            train_running_loss += loss.item()
            valid_running_loss += loss_fn(net(X_valid),y_valid).item()
        
        train_loss.append(train_running_loss)
        valid_loss.append(valid_running_loss)
        
        _, y_pred_train = torch.max(net(X),axis=1)
        train_accuracy.append((y_pred_train == y).sum().item()/len(y))
        _, y_pred_valid = torch.max(net(X_valid),axis=1)
        valid_accuracy.append((y_pred_valid == y_valid).sum().item()/len(y_valid))


print(len(train_loss))

plt.plot(train_loss,label="train-loss")
plt.plot(valid_loss,label='valid-loss')
plt.legend()
plt.show()

plt.plot(train_accuracy,label="train-accuracy")
plt.plot(valid_accuracy,label="valid-accuracy")
plt.legend()
plt.show()