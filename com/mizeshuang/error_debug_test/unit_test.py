# 对于测试驱动开发熟悉的那么对于单元测试应该不会陌生
# 单元测试是用一个模块或者函数，或者一个类来对正确性工作进行的测试
# 比如对于abs()函数
# 1 输入1、1.2、0.99 .期待返回的值与输入的相同
# 2 输入-1、 -2 、-0.99 期待返回的值与输入的相反
# 3 输入0 期待返回0
# 4 输入非数值如None {} [] () 期待抛出TypeError错误
# 将上面的测试用例放到一个测试模块里面的话就构成了一个完整的单元测试
# 这种测试的方式就让我们很好的对于我们改过的代码进行一个测试，然后保障代码的健壮性
# 下面我们定义一个我们自己的MyDict类
class MyDict(dict):
	"""docstring for MyDict"""
	def __init__(self, **kw):
		super(MyDict, self).__init__(**kw)
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'MyDict' has no attribute '%s'" % key)
	def __setattr__(self, key, value):
		self[key] = value
# 为了编写一个单元测试，我们需要引入python自带的unittest模块，编写mydict_test.py

