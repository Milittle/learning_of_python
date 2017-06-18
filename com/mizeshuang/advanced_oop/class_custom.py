# 定制类
# 使用__xx__这种变量进行类的定制
# 我们已经知道了，__len__()函数和__slots__()函数的作用
# __str__()函数的使用，这个函数就是定义类实例的打印名字
class Student(object):
	"""docstring for Student"""
	sum = 1000
	def __init__(self, name):
		super(Student, self).__init__()
		self.name = name
	def __str__(self):
		return 'Student Object (name: %s)' % self.name
	__repr__ = __str__
	def __iter__(self):
		return self
	def __next__(self):
		self.name = self.name + 'e'
		if len(self.name) > 50:
			raise StopIteration()
		return self.name
	def __getitem__(self,n):
		if isinstance(n,int):
			a,b = 1,1
			for i in range(n):
				a,b = b,a + b
			return a
		elif isinstance(n,slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for i in range(stop):
				if i > start:
					L.append(a)
				a, b = b, a + b
			return L
	def __getattr__(self,attr):
			if attr == 'score':
				return 99
			if attr == 'age':
				return lambda : 25
			raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
	def __call__(self):
		return 'My name is %s' % self.name
s = Student('Milittl')
print(s)
# 如果不定义上面的__str__函数的话，打印的是<__main__.Student object at 0x0141A370>
# 定义了__str()__函数以后打印的是Student Object (name: mizeshuang)
# 还有一个函数是为调试服务的函数，就是调试的时候当调试在变量的时候就会显示该变量的名字
# 这个函数就是__repr__()

# __iter__()函数和__next__()函数
# 这两个函数的前面是返回这个对象的迭代器对象，然后利用for循环调用__next__()函数进行对象的访问
# 直到遇到遇到StopIteration异常
for i in s:
	print(i)

# __getitem__()
# 这个就是list的那个取元素的函数支持
print(s[1])

# 但是list有切片
# 就在这里面进行判断
print(s[:12]) #如果要令该类使用起来和list一样的话，需要定义处理步长和对负数的索引进行支持

# __getattr__()
# 通常我们调用一个类没有的属性的时候就会报错
# print(s.score) # AttributeError: 'Student' object has no attribute 'score'
# 添加上面这个函数就会默认返回一个函数
# print(s.score) # 99
# 而且如果定义了__getattr__()函数的话，以后访问该类不存在的属性的话就会返回None，
# 所以要报错的话需要抛出异常
# print(s.abc) # AttributeError: 'Student' object has no attribute 'abc'

# 定义一个chain类
class Chain(object):
	def __init__(self,path = ''):
		self._path = path
	def __getattr__(self,path):
		return Chain('%s/%s' % (self._path,path))
	def __str__(self):
		return self._path
print(Chain('api').status.user.timeline.list)

# __call__()
# 这个函数的实现是对实例对象的直接调用是否支持
print(s())

# 全局的callable()函数时刻以检测一个变量是否支持函数调用
print(callable(s)) # True支持调用
