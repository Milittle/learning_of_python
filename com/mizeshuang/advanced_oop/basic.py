# 基本的介绍
# 对于python的类来说
# 1. 可以将属性和方法动态绑定在对象上，也可以绑定在类上面
# 2. 而且在面向对象的编程里面可以有封装、继承、多态这三种特性
# 下面对类的实现以及对象实例的属性和方法的动态绑定
class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		super(Student, self).__init__()
		self.name = name
# 上面是一个Student类
# 下面生成实例和动态绑定属性和方法
s = Student('mizeshuang')
s.age = 12 # 绑定属性
print(s.age)
def get_name(self):
	return self.name
from types import MethodType
s.get_name = MethodType(get_name,s) # 绑定方法,实例绑定属性的方式只有这么做才可以，不与类绑定方法一样
print(s.get_name()) # 但是此处的方法只会在该队想上面有，为了让所有的对象都有，就就要绑定在类上面
Student.get_name = get_name # 这就绑定在了该类上面

s2 = Student('guo')
print(s2.get_name()) # 给类绑定了get_name()方法以后，以后的实例对象就都能用get_name()方法了
