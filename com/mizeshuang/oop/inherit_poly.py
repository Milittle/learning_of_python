## 继承和多态
class Animal(object):
	def run(self):
		print('Animal is running')
class Dog(Animal):
	def run(self):
		print('Dog is running')
class Cat(Animal):
	def run(self):
		print('Cat is running')
dog = Dog()
cat = Cat()
dog.run()
cat.run()
# Dog is running
# Cat is running
# 从运行结果来看，这就是类的多态
# 在每个动物类继承了父类的类以后，重新实现了run方法，这就能进行分别的调用
# 继承的好处
# 1. 实现多态
# 2. 子类可以进行私人定制
# 3. 重复的功能可以进行重复利用
# 4. 符合高内聚，低耦合原则

# 使用isinstance函数可以检测类对象的
# 只要是继承的父类，这个函数也可以检测为父类对象
# 这就是多态的使用
print(isinstance(cat,Animal)) # True

# 下面用一个例子来进一步说明多态的好处
def run_twice(animal):
	animal.run()
	animal.run()
## 上面的这个函数的意思就是，传入一个animal对象，这样它的子类可是这个对象，但是通过多态的特性，子类就会分别调用相对应的run函数
run_twice(cat) ## 打印两遍的run函数信息


## 还有类继承是符合开闭原则的
# 开：是对继承开放
# 闭：是对元类修改的关闭
# 继承其实就是一颗继承树


## 这里说明一个道理，就是python是动态语言
# 考虑上面的例子，run_twice这个函数，其实可以传入任意有run方法的类对象，因为没有所谓的类型限制
# 这是因为在python中在传递参数的时候是没有限制参数类型的，所以这就是动态语言和静态语言的一个区别
# 这种现象说明在动态语言中，就是看起来像就可以做，这也称为鸭子类型
# 所以说一般对象实例不能和类属性名字一样