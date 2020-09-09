# expand vs repeat
# 扩展维度  expand 需要时再拓展，repeat则是直接扩展， 前者更节约内存，推荐
import numpy as np
import torch

a = torch.rand(2,4)
b = torch.rand(1,2)
print(a, b)

# 维度拓展: 注意——只能对为1的维度进行拓展
c = b.expand(2,2)
print(c.shape, c)

# repeat 拓展： 参数指的是在某一个维度 拷贝 n 次
d = c.repeat(2,2)   # 拷贝第一个维度 4 次， 第二个维度 5 次
print(d.shape, d)   # 8*10 的向量


# .t() 转置操作只能用于 2D向量，对于高维向量报错
# transpose + view 操作可能导致的信息丢失， 记得对 view 进行跟踪。

# permute 维度交换利器
f = torch.rand(2,3,4,3)
print(f.shape)
g = f.permute(3,2,1,0)   # 将第三个维度放在最前，其余依次
print(g.shape)

# 注意：tranpose 和 permute 涉及维度交换， 一定会将数据的内存顺序打乱

