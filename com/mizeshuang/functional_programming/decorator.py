## 顾名思义，就是装饰器
# 这个装饰器就是给现有函数加功能的
# 加完功能就是返回函数
from functools import wraps
## 接下来我们做一个很小的实例
def decorator(f):
    def wrapper(*args,**kwargs):
        print('this is hello word function')
        f(*args,**kwargs)
    return wrapper

@decorator ## 这个是一个python加上装饰器的快捷做法
def f():
    print('hello world')
# 接下来我们给f加上一些功能
## 让我们来调用一下
f()
## this is hello word function
## hello world
## 上面就是这个函数打印的结果，这个很神奇

## 那我们下面在弄一个比较复杂的，带有参数的装饰进去

def dec(text):
    def wrapper_outside(func):
        @wraps(func)## 这个地方用来修改当前函数名字，需要与装饰的原函数名字相同
        def wrapper_inside(*args,**kwargs):
            print('this is %s function' % text)
            func(*args,**kwargs)
        return wrapper_inside
    return wrapper_outside
@dec('f_t')
def f_t():
    print('hello agin')
f_t()
print(f_t.__name__)

## 上面输出了函数的名字，从一个f_t变为了我们定义的内置函数，也就是返回给该函数的那个内置函数
# 那么我们需要去修改它
# 怕以后的代码会出错
# 有些依赖函数签名的代码会出错的
## 所以在内置返回的那个装饰器函数前面加一个@functools.wraps(func)
# 这个代码的作用就是将内置函数的名字改为这个函数的名字
# 因为functools是一个python内置模块
# 所以我们需要引入模块

## 那么最后就是一般通过类来实现的decorator也是可以的
# 因为在设计模型中就是有这个设计模式
# 也就是装饰者模式