# 定制类
# 使用__xx__这种变量进行类的定制
# 我们已经知道了，__len__()函数和__slots__()函数的作用
# __str__()函数的使用，这个函数就是定义类实例的打印名字
class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		super(Student, self).__init__()
		self.name = name
	def __str__(self):
		return 'Student Object (name: %s)' % self.name
s = Student('mizeshuang') 
print(s) # 如果不定义上面的__str__函数的话，就不会打印Student Object (name: mizeshuang)
