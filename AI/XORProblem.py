import numpy as np
 
def sigmoid(x): return 1 / (1 + np.exp(-x))
def sigmoid_d(x): return x * (1 - x)
 
# XOR problem — a simple neural net test
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])
 
np.random.seed(42)
W1 = np.random.randn(2,4) * 0.5   # Input→Hidden weights
W2 = np.random.randn(4,1) * 0.5   # Hidden→Output weights
 
lr = 0.5  # Learning rate
losses = []
 
for epoch in range(10000):
    # Forward pass
    h = sigmoid(X @ W1)
    o = sigmoid(h @ W2)
 
    # Loss (Mean Squared Error)
    loss = np.mean((y - o)**2)
    losses.append(loss)
 
    # Backward pass — compute gradients
    d_o = (o - y) * sigmoid_d(o)
    d_h = (d_o @ W2.T) * sigmoid_d(h)
 
    # Update weights
    W2 -= lr * h.T @ d_o
    W1 -= lr * X.T @ d_h
 
import matplotlib.pyplot as plt
plt.plot(losses); plt.title('Loss Decreasing During Training')
plt.xlabel('Epoch'); plt.ylabel('Loss'); plt.show()
 
print('Final predictions (should be close to [0,1,1,0]):')
print(np.round(o, 2))
