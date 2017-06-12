# 类与实例
# 面向对象的最重要的概念就是类和实例，类是抽象的模板
# 下面以Student为例子进行说明类
# 在类中定义的函数，第一个参数永远都是self，但是在传参的时候不需要给参数
class Student(object):
	def __init__(self,name,score): # 在类中定义初始化参数
		self.name = name
		self.score = score
	def print_info(self):
		print('name: %s,score: %s' % (self.name,self.score))
# 这里面class后面紧跟着类的名字Student
# 括号里面的是该类继承的类名字
# 在python中，默认的主类就是object
bart = Student('mizehsuang',100)
print(bart) #可以看出bart是一个对象
#<__main__.Student object at 0x02B7A370>
# 它的内存地址和其他的对象的内存地址是不一样的
# 而Student是一个类
print(Student) #<class '__main__.Student'>


# 可以给对象任意的绑定属性
# 下面的操作就是绑定属性的操作
bart.name = 'mizeshuang'
print(bart.name) # mizeshuang

# 因为类是对象的模板
# 那么就可以在创建类的时候就可以进行参数初始化
# 在类的定义上面

# 我们需要进行封装
# 这也是面向对象的一大特性之一
# 比如将name、score打印出来的函数
# 封装的特性就是将类里面的属性，通过函数的方式进行访问
# 虽然python支持直接访问属性的值，而且甚至可以直接修改
# 这一特性不知道是不是提倡的使用，应该是不提倡的
# 因为在类中就是要对外封装
# 比如Student里面的print_info函数
# 打印name信息和score信息
# 对于类的不同对象，每个实例包含的属性有可能不一样
# 因为python可以动态绑定属性
