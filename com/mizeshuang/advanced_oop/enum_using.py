# 枚举类的介绍
# 使用Enum类定义枚举类
# 里面的变量是从1开始编号，里面包含名字和成员成员是
from enum import Enum, unique
month = Enum('m',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
for name,member in month.__members__.items():
	print('name ->' ,name, ',',member,member.value)


# 也可以通过继承Enum类来实现它
@unique # 这个装饰器对于该枚举类的唯一性做出检测
class MyEnum(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wes = 3
	Thu = 4
	Fri = 5
	Sat = 6
	def __init__(self, arg):
		self.arg = arg
print(MyEnum.Wes.value)
print(MyEnum['Wes'].value)
print(MyEnum(0).value)
	
	

