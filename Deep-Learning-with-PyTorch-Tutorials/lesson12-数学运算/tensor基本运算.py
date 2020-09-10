# + - * /   对于1维向量

# 对于矩阵乘法
# 1. * 表示对应元素相乘
# 2. torch.mm 和 torch.matmul， @ 表示矩阵乘法。 Torch.mm 只适用于2维向量的矩阵乘法
#  @ 是 torch.matmul 的运算符重载
import torch
a = torch.ones(2,2)*3
b = torch.ones(2,2)
print(a, b)

print(torch.mm(a,b))
print(a*b)
print(a@b)

# rsqrt()  平方根的倒数
aa = torch.full([2,2], 9.)
print(aa)
print(aa**2)
print(aa.sqrt())
print(aa.rsqrt())

# 求指数
a = torch.exp(torch.ones(2,2))
print(a)
print(torch.log(a))  # 默认以e为底求对数


# 近似函数
# 1. floor() 向下取整
# 2. ceil()  向上取整
# 3. trunc() 截取整数
# 4. frac() 截取小数
a = torch.tensor(3.14)
print(a.floor(), a.ceil(), a.trunc(), a.frac())
print(a.round())   # round 四舍五入


# clamp 裁剪  ---- 一般用于梯度裁剪
grad = torch.rand(2, 3)*15
print(grad.max())
print(grad.median())
print (grad)
print(grad.clamp(10))    # 限制每个元素最少取10， 小于10的都变成10
print(grad.clamp(0,10))  # 限制取值为 (0, 10)  大于10的都变成10



