# 列表生成式 是python内置的非常简单却强大的可以用来创建list的生成式
# 举例子，比如生成list [1,2,3,4,5,6,7,8,9,10] 可以使用list(range(1,11))来生成
import os
list(range(1,11))
print(list(range(1,11)))
# 生成[1X1,2X2,...,10X10]的list
x = [i * i for i in range(1,11)]
print(x)
# 如果需要条件的话，也可以加上条件
y = [j * j for j in range(1,11) if j%2==0]
print(y)
# 还可以使用双循环，形成全排列
z = [w + t for w in 'ABC' for t in 'XYZ']
print(z)
# 输出所有文件和目录
print([d for d in os.listdir()])
# for循环可以使用两个甚至多个变量，比如dict的item()可以同时迭代key和value：
d = {'x':'A','y':'B','z':'C'}
for k,v in d.items():
    print(k,'=',v)
# 因此列表生成式可以使用两个变量来生成list
two = [k+'='+v for k,v in d.items()]
print(two)
# 将list中的字符都变为小写
L = ['Hello','World','SHEEELL']
l = [o.lower() for o in L]
print(l)
# 使用内置函数检测是否为字符串
print(isinstance('123',str))
print(isinstance(123,str))
