# 使用元类
# 在python中，是利用type()这个函数来创建类的
class Student(object):
	def __init__(self,name = 'default'):
		self.name = name
s = Student('mizeshuang')
print(type(Student)) # <class 'type'> 元类类型
print(type(s)) # <class '__main__.Student'> 是Student类型

# 使用type来定义一个类

def fn(self,name = 'world'):
	print('hello, %s' % name)
	return '你好'
Student = type('Student',(object,),dict(hello = fn))
s1 = Student()
print(type(s1))
s1.hello()

# metaclass类很重要
# 简单的来说就是，metaclass是创建类的模板
# 下面创建一个metaclass来为我们自定义的MyList类添加一个add方法
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		print(cls, name, bases, attrs)
		return type.__new__(cls, name, bases, attrs)
# 现在有了metaclass以后那么在创建一个新类的时候
# 需要在创建类的时候传入metaclass参数指定创建这个类的元类
class MyList(list, metaclass = ListMetaclass):
	pass
# 上面的类就说明MyList这个类需要使用ListMetaclass这个元类的ListMetaclass.__new__()来创建
# 我这里的猜想是这个MyList类就不需要通过type函数来创建了
# __new__()参数的意义：
# 1 cls当前准备创建类的对象 # <class '__main__.ListMetaclass'>
# 2 类的名字 # MyList
# 3 类继承的集合 # (<class 'list'>,)
# 4 类方法的结合 # {'__module__': '__main__', '__qualname__': 'MyList', 'add': <function ListMetaclass.__new__.<locals>.<lambda> at 0x035A70C0>}
# 测试一下这个MyList类的add方法
my_list = MyList()
my_list.add(1)
my_list.add(2)
print(my_list)
# 在上面的metaclass中其实就是修改类的定义的
# 接下来我们使用ORM 对象-关系映射连接数据库的例子来说明这个元类的强大之处
# 我们现在使用这个元类来创建一个ORM框架
# 1 将调用接口写出来,这就是使用者来写的功能函数
# class User(Model):
# 	id = IntegerField('id')
# 	name = StringField('name')
# 	email = StringField('email')
# 	password = StringField('password')
# 创建实例
# user = User(id = 12345, name = 'Milittle', email = 'test@orm.org', password = 'my-pass')
# 保存数据库
# user.save()
# 在上面的类中，Model、IntegerField、StringField这个就是我们ORM框架提供的
class Field(object):
	def __init__(self, name, column_type):
		self.name = name
		self.column_type = column_type
	def __str__(self):
		return '%s:%s' % (self.__class__.__name__, self.name)
class IntegerField(Field):
	def __init__(self,name):
		super(IntegerField,self).__init__(name, 'bigint')
class StringField(Field):
	def __init__(self,name):
		super(StringField,self).__init__(name,'varchar(100)')
class ModelMetaclass(type):
	def __new__(cls, name, bases,attrs):
		if name == 'Model':
			return type.__new__(cls, name, bases, attrs)
		print('Founding Model: %s' % name)
		mappings = dict()
		for k, v in attrs.items():
			if isinstance(v, Field):
				print('Found mapping: %s ==> %s' % (k, v))
				mappings[k] = v
		for k in mappings.keys():
			attrs.pop(k)
		attrs['__mappings__'] = mappings # 保存属性和列的映射关系
		attrs['__table__'] = name # 保存表明和类名一样
		return type.__new__(cls, name, bases, attrs)
class Model(dict, metaclass = ModelMetaclass):
	def __init__(self, **kw):
		super(Model, self).__init__(**kw)
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError as e:
			raise AttributeError(r"'Model' object has no attribute '%s'" % key)
		else:
			pass
		finally:
			pass
	def __setattr__(self, key, value):
		self[key] = value
	def save(self):
		fields = []
		params = []
		args = []
		for k, v in self.__mappings__.items():
			fields.append(v.name)
			params.append('?')
			args.append(getattr(self, k, None))
		sql = '	insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
		print('SQL: %s' % sql)
		print('ARGS: %s' % str(args))
class User(Model):
	id = IntegerField('id')
	name = StringField('name')
	email = StringField('email')
	password = StringField('password')
user = User(id = 12345, name = 'milittle', email = '4356@org.com', password = '123456')
user.save()
