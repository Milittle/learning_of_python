## 这是匿名函数的介绍以及代码测试
## 匿名函数的关键字就是lambda
# 使用map函数的例子是很恰当的
print(list(map(lambda x: x * x,[1,2,3,4,5,6,7,8,9])))

# lambda是关键字，后面冒号之前的是参数，后面的是表达式，没有返回值，也不需要返回值
# 而且lambda也可以当作返回值
def build(x):
    return lambda:x * x
print(build(2))
## 返回的就是匿名函数
# 但是可以赋值给变量
f = build(5)
print(f())
## 以上就是对lambda返回的函数进行调用的结果进行了验证