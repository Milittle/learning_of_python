# 这是python里面的一个特殊变量
# 在类里面定义这个对象的tuple，能限制类实例的动态绑定的属性名
class People(object):
	"""docstring for People"""
	"""__slots__"""
	__slots__ = ('name','age','birth') #这个说明这个类实例对象能有name、age、和birth这三个属性，但是通过类绑定可以添加属性的范围
	def __init__(self, name):
		super(People, self).__init__()
		self.name = name
p = People('mizeshuang')
People.l = 123 # 但是通过类动态绑定就可以
print(p.l)
# p.k = 456 # IndentationError: unexpected indent
# p.l = 456 # AttributeError: 'People' object attribute 'l' is read-only
# 虽然通过类添加了属性，但是只读的属性，就是只能第一次赋值
