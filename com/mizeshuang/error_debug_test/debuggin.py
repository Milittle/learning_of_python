# 这个调试就是将程序但不执行，或者设置断点进行调试
# 1 第一种方式就是在执行的时候使用print()函数打印一些变量的信息，这是我们之前的python编程中经常使用的方式
# 2 断言就是用assert这个关键字来定义断言，其实就是当这个表达式判断为假的时候就会抛出AssertError的错误
# 其实相比print()来说assert的性质也差不多，只不过是可以通过 -O参数关闭assert的检测
# 3 就是利用loggin这个模块了，前两种就不进行演示了
import logging
import pdb
logging.basicConfig(level = logging.INFO) # 这句话是必要的，因为在下面要显示loggin信息的话必须添加这句语句
# 在这里也有什么DEBUG、ERROR、WARING and so on
s = '0'
n = int(s)
pdb.set_trace() # 运行到这里以后自动停止，也就是正常运行，运行的时候不需要加入 -m pdb
logging.info('n = %d' % n)
# print(10/n) # ZeroDivisionError: division by zero

# 4 那就是pdb，也就是python debug
# python -m pdb debugging.py 用这样的方式进行pdb的调用
# 进去调试模式以后：
# l 查看附近的代码
# n 执行下一步
# p 变量名 可以查看变量的信息
# q 退出调试模式
# 据我观察 s 是进入调试

# 5 我们还可以设置断点，直接运行到该断点进行执行
# 上面我们设置了断点

# 6 我们还可以使用IDE比如PyCharm

# 最后还要强调的是其实我们用到的loggin还是挺多的