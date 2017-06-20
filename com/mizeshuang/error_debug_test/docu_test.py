# 文档测试，经常阅读python官方文档
# # 会有一些类似下面这样的代码
# >>> import re
# >>> m = re.search('(?<=abc)def', 'abcdef')
# >>> m.group(0)
# 'def'
# 可以将这些代码在交互环境里面进行执行，得到的结果和上面的一致
# 这些注释代码是直接粘粘贴在代码里面的
# 那么我们可不可以直接执行这些在注释里面的代码
# 答案是肯定的
# def abs(n):
# 	'''
# 	Function to get absolute value of number.
# 	Example:
# 	>>> abs(1)
# 	1
# 	>>> abs(-1)
# 	1
# 	>>> abs(0)
# 	0
# 	'''
# 	return n if n >= 0 else (-n)
# python自身带有doctest模块
# 让我们来测试上次编写的MyDict这个类