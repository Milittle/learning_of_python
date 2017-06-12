# 获取类型
print(type('1230'))
print(type(123))
print(type([1,2,3]))
print(type((1,2,3,44,5)))
print(type({'name':'mizehsuang','age':123}))
print(type(1.23))
## type函数可以获得一个实例的类型
## 但是要判断一个函数或者其他类型的时候，需要引入types这个模块来调用那些函数类型还有特殊的生成器类型
# 进而可以判断一个实例的对象类型

class People(object):
	def __init__(self):
		print('super People')

class Student(People):
	def __init__(self):
		super(People,Student).__init__(self)
		print('sub class Student')
s = Student()
print(type(s) == People) ## 但是这个只能是输出子类,所以检测为父类的时候就为False
## 所以一般检测这种类型的时候就用isinstance函数


## 用dir()函数可以直接获取一个对象的所有属性和函数
## 类似于__xx__这种名字是特殊的变量，比如自定义__len__()方法，是为这个对象提供len()函数支持的
# 光列出这些属性和函数是不够的
# 我们需要配合getattr(),setattr()以及hasattr()这些方法进行属性的操作
class MyObject(object):
	def __init__(self,x):
		self.x = x
	def power(self):
		return self.x * self.x
obj = MyObject(123)
print(hasattr(obj,'x')) ## 这是判断obj这个对象里面有没有x这个属性(函数)
print(hasattr(obj,'power')) ## 这是判断obj这个对象里面有没有x这个属性(函数)
setattr(obj,'y',789) # 这是给obj这个对象添加属性y 在这里我想应该会有添加函数的方法，只不是后面的式子会复杂一些（也就是第三个参数）
print(getattr(obj,'y',456)) # 获取obj这个对象的属性y,还可以添加默认值，如果没有这个属性的话就返回默认值
f = getattr(obj,'power')
print(f()) ## 和调用obj.power()效果是一样的
