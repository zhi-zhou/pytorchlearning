# merge or split

# cat
import torch
a = torch.rand(4, 32, 8)
b = torch.rand(5, 32, 8)
c = torch.cat([a,b],dim=0)  # 将 a, b 在第0个维度上拼接
print(a.shape, b.shape, c.shape)
# cat 需要的条件，除了拼接维度之外，其他维度必须一致

# stack 创建了一个新的维度
import torch
a = torch.rand(4, 3, 32, 32)
b = torch.rand(4, 3, 32, 32)
c = torch.stack([a, b], dim=2)   # 在第二个维度之前插入一个新的维度，合并a,b
print(a.shape, b.shape, c.shape)

a = torch.rand(2,3)
b = torch.rand(2,3)
c = torch.stack([a,b], dim=1)
print(c.shape)
print(a, b, c)
# stack 要求两者维度 必须一模一样

# split: 根据长度拆分.
# 如何要拆分出的向量，指定维度长度一致，则参数为 一个长度值
# 如何要拆分出的向量，指定维度长度不一致，则参数为 一个list, list中值和要等于拆分维度值
print(c.shape)
aa, bb, cc= c.split(1, dim=2)   # 在第3个维度上，拆分成长度为1的向量
print(aa.shape, bb.shape, cc.shape)
dd, ee = c.split([1,2], dim=2)
print(dd.shape, ee.shape)

# chunk: 按照数量来拆分
print(c.shape)
aa, bb = c.chunk(2, dim=0)   # 在第0个维度上，将c平均拆为两份
print(aa.shape, bb.shape)