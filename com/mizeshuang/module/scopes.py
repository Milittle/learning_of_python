## 这个说明作用域这个概念
# 作用域就是说，在一个模块中可以定义各种各样的变量和函数
# 有的想让外界访问，但是有的不想让外界访问
# 这里面就有控制机制
# 可以在变量和函数前面加 '_' 这个符号来说明
# __xxx__这种变量是特殊的变量
# 类似于_x,__xx这种的变量是非公开的，不建议直接引用
# 其实在这里说明一个问题就是，python没有特定的限制不能引用
# 只是对于程序员来说，要自觉不能去引用
# 这种不建议直接引用的变量或者函数，我们可以提供其他接口进行访问
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
## 这样greeting函数就包装了上面两个private函数，让外界可以进行访问