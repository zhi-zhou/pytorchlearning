# 使用 numpy 实现两层神经网络
# 1. 一个全连接 Relu神经网络，一个 隐藏层， 没有bias.   用来从x预测y, 使用L2  Loss
#    公式： h = W1*X + b1
#           a = max(0, h)
#           y_hat = W2a+b2    两层神经网络
# 这一实现 完全使用 numpy 来计算前向神经网络，loss 和 反向传播

# numpy ndarray 是一个简单的n维array, 它不知道任何关于深度学习，梯度，以及计算图的知识，它只是一种用来计算数学运算的数据结构


