# 错误的处理，这里就是当python代码出现了错误应该怎么去处理
# try... except... else... finally
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
# 主要是看这个网址中的错误类型的继承关系，然后就可以捕获错误了
# 下面用一个实例来说明这个类型
def division(n,m):
	try:
		print('try...')
		n/m
		print('result...')
	except ZeroDivisionError as e:
		print('except:',e)
	else:
		print('execute else not except')
	finally:
		print('finally...') # 这就是在return语句以后也会执行的finally
division(10,0)
# try...
# except: division by zero
# finally...
division(10,1)
# try...
# result...
# execute else not except
# finally...


# 记录错误就是将错误信息进行一个栈运行，所以在显示错误的时候，就需要查看错误栈
# 抛出错误用raise关键字
# 就是将错误抛到上一层调用该函数的结构当中，在这层不进行处理
