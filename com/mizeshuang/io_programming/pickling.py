# 序列化，在python里面叫picking
# 在其他语言中也叫serialization、marshalling、flattening
# 分别用pickle来做序列化和反序列化
import pickle
d = dict(name = 'mi',age = 10,score = 100)
# 这个方法会将一个对象序列化成二进制数，只不过是用十六进制表示dumps方法
print(pickle.dumps(d))

# 还有一个dump方法就是直接将对象序列化而且写入一个文件中dump方法
f = open('./temp.txt','wb')
pickle.dump(d,f) # b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x02\x00\x00\x00miq\x02X\x03\x00\x00\x00ageq\x03K\nX\x05\x00\x00\x00scoreq\x04Kdu.'
f.close()

# 直接从一个二进制字符串中反序列化字符串loads方法
str = b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x02\x00\x00\x00miq\x02X\x03\x00\x00\x00ageq\x03K\nX\x05\x00\x00\x00scoreq\x04Kdu.'
print(pickle.loads(str))

# 从文件中反序列化的方法load
f_result = open('./temp.txt','rb')
d_result = pickle.load(f_result)
f_result.close()
print(d_result) # {'name': 'mi', 'age': 10, 'score': 100}

# 这上面的pickle模块是将python中的数据序列化为二进制数
# 但是其他语言中就不能支持
# 所以一般序列化为JSON比较普遍的
# JSON是各种不同语言传递对象的一种方法
# python这里就不做介绍，可以去www.json.org这个网站上面自行学习


# 下面开始将列出python中json序列化对象的支持
import json
d_json = {'age':18,'name':'mi'}
print(json.dumps(d_json)) # {"age": 18, "name": "mi"}

# 下面是用json写入一个file-like object
f_json = open('./temp.txt','w')
json.dump(d_json,f_json)

# 当然也可以使用load函数进行反序列化的操作
j_f = '{"age":12,"name":"milittle"}' # 注意这里必须是json字符串,而且在json中，字符串是双引号，不和python里面的单引号一样
print(json.loads(j_f))


# 1下面就是重中之重，我们一般不会傻傻的就会使用dict这个对象
# 也不会只用json模块转换这个对象为json字符串
# 我们用的更多的是对象，也就是将类的实例进行序列化
# 下面我们定义一个类，对它的实例进行一个实例化操作
class Student(object):
	def __init__(self,name,age,score):
		self.name = name
		self.age = age
		self.score = score
#创建类的实例
s = Student('milittle',20,100)
# 上面的这个对象现在还不能直接拿json的dumps方法进行序列化，因为它不认识
# print(json.dumps(s)) # TypeError: Object of type 'Student' is not JSON serializable
# 他会这么提示错误
# 下面我们定义一个方法，辅助这件事做成功
def student2json(std):
	return{
		'name':std.name,
		'age':std.age,
		'score':std.score
	}
s1 = Student('mi',20,99)
print(json.dumps(s1,default = student2json)) # {"name": "mi", "age": 20, "score": 99}
# 这次就能做了，这是因为我们传入了default函数，来帮json.dumps这个方法理解这个对象的
# 或者我们偷懒，直接将Student对象转化为dict
print(json.dumps(s1,default = lambda obj:obj.__dict__)) # {"name": "mi", "age": 20, "score": 99}一样的效果

# 那么要反序列化的话，就需要另一个函数的支持了
# 1 首先将json字符串用loads方法将json字符串转化为dict然后在将dict转换为Student

s_json = '{"name": "mi", "age": 20, "score": 99}'
s_dict = json.loads(s_json)
def dict2student(std):
	return Student(std['name'],std['age'],std['score'])
student = dict2student(s_dict)
 
print(student.name,student.age,student.score) # mi 20 99

# 以上就是json对于对象的支持
# 总结就是使用pickle是内部，使用json是外部
# 分别有dumps、dump、loads、load方法来保障序列和反序列