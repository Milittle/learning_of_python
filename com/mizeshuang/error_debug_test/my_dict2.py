import doctest
class MyDict(dict):
	# 这里需要注意的是需要在>>>后面加上空格，不然会出错误的
	"""
	Simple dict but also support access as x.y style.
	>>> d1 = MyDict()
	>>> d1['x'] = 100
	>>> d1['x']
	100
	>>> d1.y = 200
	>>> d1['y']
	200
	>>> d2 = MyDict(a=1,b=2,c='3')
	>>> d2.c
	'3'
	>>> d2['empty']
	Traceback (most recent call last):
		...
	KeyError: 'empty'
	>>> d2.empty
	Traceback (most recent call last):
		...
	AttributeError: 'MyDict' has no attribute 'empty'
	"""
	def __init__(self, **kw):
		super(MyDict, self).__init__(**kw)
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'MyDict' has no attribute '%s'" % key)
	def __setattr__(self, key, value):
		self[key] = value
if __name__ == '__main__':
	doctest.testmod()
# doctest测试很好用，不但可以做测试，也可以通过某些文档工具就可以将doc注释提出出来，用户在看文档的时候
# 也可以看到doctest的程序