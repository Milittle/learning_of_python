## 当我们介绍高阶函数的时候
# 使用的是函数当作参数传递
# 既然这样说明函数也可以当作返回参数返回给外层
# 所以我们先定义一个普通函数
def sum_of_number(*args):
    s = 0
    for i in args:
        s += i
    return s
## 上面这个函数使用了普通的模式，定义了求和函数
# 下面我们调用一个
print(sum_of_number(1,2,3,4,5))

## 但是现在提出一种新的需求
# 就是当现在时期不适用求和函数
# 只不过是要求和
# 这有点难说，就是说不要结果，但要计算结果
# 所以这就有用了
def sum_of_return_function(*args):
    def return_function():
        s = 0
        for i in args:
            s += i
        return s
    return return_function
## 那么我们接下来测试一下
f = sum_of_return_function(1,2,3,4,5,6)
print(f)
print(f())
## 上面第一个式子输出的是<function sum_of_return_function.<locals>.return_function at 0x03547030>
# 上面第二个式子是求和的结果
# 这个意思就是返回的是一个函数
# 所以明白了这是一个怎么回事了
# 而且每次返回的参数都不一样


## 还有一个概念就是闭包
# 这个概念在这个地方就是用大白话说
# 他就是将返回函数所用到的局部变量进行的封装打包
# 而且在调用她的时候会用
# 所以也就遇到了一个很至关重要的问题就是
# 不能在局部中使用循环变量
# 这样的可能性就是多次返回这个返回的封装以后
# 里面的循环变量就会变化，从而让结果失真


## 下面用实验进行说明
def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1,f2,f3 = count()
print(f1(),f2(),f3())
## 那么你会发现这个结果都是9，这个就造成了闭包的错误
# 一般不要把函数放在循环里面
## 重新定义函数，是的功能正常
def count1():
    def f(j):
        def b():
            return j * j
        return b
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
ff1,ff2,ff3 = count1()
print(ff1,ff2,ff3)
print(ff1(),ff2(),ff3())
## 以上的功能是正常的
# 所以在编写返回函数的功能的时候
# 一定提前思考好
# 这个代码应该怎么写
# 逻辑是正常的

