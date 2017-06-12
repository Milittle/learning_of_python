# 这是对象属性和类属性的区分
# 类属性可以直接在定义类的时候直接定义
# 对象属性可以在生成对象以后进行绑定
# 给类定义属性的时候，这个属性属于每一个实例对象
# 但是如果实例对象新绑定了与类属性一样的名字的话，这个类属性就被覆盖了，实例对象只能访问到他自己访问的属性
class Student(object):
	name = 'Student'
	def __init__(self):
		print('init')
s = Student() # 定义类的具体实例
print(s.name)
s.name = 'mizeshuang' # 此时类属性name已经被覆盖了
print(s.name) 
print(Student.name) # 类的属性可以直接访问
del s.name # 删除s对象的属性
print(s.name)