# 这里的多重继承就是，一个类但作为很多类的子类的时候
# 不需要进行单一继承，一直下去，python是支持多继承的
class Wisedom(object):
	"""docstring for Wisedom"""
	def __init__(self, arg):
		print('Wisedom')
		self.arg = arg
class Men():
	"""docstring for Men"""
	def __init__(self, arg):
		print('Men')
		self.arg = arg
class Super_Men(Wisedom,Men):
	def __init__(self,name):
		self.name = name
s_men = Super_Men('mizeshuang')

print(s_men.name)

