# 使用@property定义属性
# 这个应用的场景是通过要求将属性封装而且要做类型检测提出来的方法
class Student(object):
	"""docstring for Student"""
	__slots__ = ('name','score')
	def __init__(self, name,score):
		super(Student, self).__init__()
		self.name = name
		self.score = score
	def get_score(self):
		return self.score
	def set_score(self,score):
		if isinstance(score,int) != True:
			raise ValueError('score must be int type')
		if score >= 0 and score <= 100:
			self.score = score
		else:
			raise ValueError('score must be in the 0 ~ 100')
s = Student('mizeshuang',100)
s.score = 'hello' # 这样就破坏了score的属性特性
# print(s.score)
# 所以我们想办法让这一结果正常 添加getter、setter方法去限制
# s.set_score('') # ValueError: score must be int type
# s.set_score(101) # ValueError: score must be in the 0 ~ 100
s.set_score(60) # 正常
s.score = 'hello' # 但是我们还可以通过这种方式进行改变，好像我们写的东西并没有起什么作用
# 上面写的是我们可以自觉遵守的情况下才起作用的，就是说只能通过调用方法来实现属性的操作

# 下面对这一现象进行修改，就是使用@property进行修改，直接重新定义一个类
class Test(object):
	"""docstring for Test"""
	def __init__(self, score):
		self.score = score


	@property
	def score(self):
		return self._score # 为什么这里需要在score前面加上 _ 如果不加的话就会报错  


	@score.setter
	def score(self,score):
		if not isinstance(score,int):
			raise ValueError('score must be int type')
		if score >= 0 and score <= 100:
			self._score = score
		else:
			raise ValueError('score must be in the 0 ~ 100')
# 就试试这个类的效果，看看和上面那个类有什么区别
t = Test(99) #这样就既做了检查也简化了操作
print(t.score)

# 如果要生成一个只读的属性，那么就应该只写getter方法，不屑setter方法就好
