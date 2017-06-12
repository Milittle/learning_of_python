# 限制访问中，不希望外面直接访问到变量
# 可以直接添加 __ 双下划线进行限制访问，这是私有变量的意思
class Student(object):
	def __init__(self,name,age):
		self.__name = name
		self.__age = age
	def get_name(self):
		return self.__name
	def get_age(self):
		return self.__age
	def set_name(self,name):
		self.__name = name
	def set_age(self,age):
		if age > 0:
			self.__age = age
		else:
			raise ValueError('bad age type')
s = Student('mizeshuang',24)
#print(s.__name) #AttributeError: 'Student' object has no attribute '__name'
## 上面的代码是不能够访问的，这里的AttributeError的错误就是说不能访问
# 但是要明白一件事情
# 只不过python内部是将__name命名为了_Student__name这个名字了，所以外界要是以这个名字来访问的话，也是可以的
print(s._Student__name) ## 访问那是正常的，但是python是不允许这么访问的，所以程序员知其所以然，就应该自觉遵守python代码规范

## 但是为了更好的进行属性的操作，我们可以添加setter函数和getter方法
# 添加getter方法的效果
student1 = Student('guo',21)
print(student1.get_age())

## 添加setter方法的效果
# student1.set_age(-12) #ValueError: bad age type
student1.set_age(25)
print(student1.get_age())
student1.set_name('sure')
print(student1.get_name())

## 这里需要注意两点
# 1. 是在类内部的属性有__XX__这种样式的是特殊的变量，这些在类外界是可以直接访问的
# 2. 是在类外部如果直接给实例绑定属性的话，如果名字定义的和类内部的私有变量一样的名字
# 那是新定义的属相，并不是类内部的属性，因为内内部的私有属性是前面加了前缀的
