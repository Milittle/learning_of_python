# python内建了map()函数和reduce()函数
# 先看map()函数,map()函数接收两个参数，第一个参数是一个函数，一个是Iterable,map将传入的函数一次作用到雪猎的每个元素，并把结果返回作为新的Iterator
from functools import reduce


def f(x):
    return x * x
I = map(f,range(10))
for i in I:
    print(i)

# 这就说明map函数是可以做很多事情的，比如将所有的数字转化为字符串，然后返回在一个Iterator中
s = map(str,range(10))
print(list(s))

## 接下来看看reduce的用法，reduce就是把一个函数作用在一个序列上[x1,x2,x3,x4,x5]
## 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
## 他的效果就是：这个稍微有点抽象，理解一下
# reduce(f,[x1,x2,x3,x4]) = f(f(f(x1,x2),x3),x4)

# 比如求一个序列的和，就可以用reduce来实现：
def add(x,y):
    return x + y
print(reduce(add,[1,2,3,4,5]))
## 毕竟这么用就是用来举例，所以它的功能下面这个能更好的说明：
# 将一串数转化为对应的连接整数
def fn(x,y):
    return x * 10 + y
print(reduce(fn,[1,3,5,7,9]))

## 这个例子可以说是很简单的就用代码来实现，但是下面这个例子
# 就能激起你的兴趣
# 将str转化为整数
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
print(reduce(fn,map(char2num,'13579')))

## 整理成一个str2int的函数就是：
def str2int(s):
    def fn(x,y):
        return x * 10 + y
    def str2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    return reduce(fn,map(str2num,s))
print(str2int('123456'))

## 也可以用lambda来简化一下函数

def str2int1(s):
    return reduce(lambda x,y:x * 10 + y,map(char2num,s))

print(str2int1('456789'))