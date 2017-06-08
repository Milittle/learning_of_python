#!/usr/bin/env python3
#_*_ coding:utf-8 _*_
"a test module"
__author__ = 'Milittle'

import sys

def test1():
    arg = sys.argv
    if len(arg) == 1:
        print('hello world')
    elif len(arg) == 2:
        print('Hello, %s' % arg[1])
    else:
        print('Too many args')
if __name__ == '__main__':
    test1()

## 上面这个函数每行分别代表什么意思
# 1行代表在Unix/Linux/MacOs上可以直接当作执行文件
# 2行代表.py文件的编码
# 3行代表的是该文档的注释
# 4行是创建该文件的作者
# 一下就是正文代码，一般下面开始就是模块的引入
# sys模块中的argv这个参数是命令行传入的参数集合
# 第一个参数必然是.py文件的名字
# 第二个开始就是运行该程序的人传入的参数
# 参数的集合是一个list对象
# 注意到这段代码：
### if __name__ == '__main__':
#       test()
# 这段代码的做法是，当调用这个文件的时候这个文件的__name__变量就是__main__这个名字
# 但是如果其他文件调用了这个模块
# 这里的条件就不成立
# 这就很好的避免了运行这个文件
# 就是为了测试这个模块来做的判断
# 我们在uses_module中使用这个模块就可以