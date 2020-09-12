# staticstics
# 1. norm
# 2. mean sum
# 3. prod
# 4. max, min, argmin, argmax
# 5. kthvalue, topK

import torch
# 1. norm 范数，!= normalize
a = torch.full([8], 1.)
b = a.view(2, 4)
c = a.view(2,2,2)
print(a.shape, b.shape, c.shape)
# 求 1 范数 : 所有元素相加
print(a.norm(1), b.norm(1), c.norm(1))
# 2 范数
print(a.norm(2), b.norm(2), c.norm(2))  # 根号8
# 在指定维度上求范数
# 取哪个维度的范数，最终结果就会消掉哪个维度
print(b.norm(1, dim=1))
print(b.norm(2, dim=1))
print(c.norm(1, dim=0))

# 一些其他统计： mean, sum, min, max, prod
a = torch.arange(8).view(2, 4).float()
print(a)
print(a.min(), a.max(), a.mean(), a.prod())   # prod 是累乘
print(a.sum())
print(a.argmax(), a.argmin())