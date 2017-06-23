# StringIO和BytesIO
# 我们在读取文件的时候是在本地硬盘或者在网络上读取
# 但是我们也有在内存中读取文件流的习惯
# StringIO就是从内存中读取字符串流
# BytesIO是从内存中读取字节流的类
from io import StringIO
from io import BytesIO
# 是将字符串写入该对象中

# 开始StringIO的测试
s = StringIO()
print(s.write('milittle')) # 默认返回的是该字符串的长度 8
print(s.getvalue()) # 这是获取该StringIO对象中值的方法
s.close()

# 还有就是直接将字符串对象初始化在StringIO中
s_test = StringIO('milittle')
try:
	print(s_test.read())
except Exception as e:
	raise e
else:
	print('success!!!')
finally:
	s_test.close()

# 开始BytesIO开始测试
# 这个和上面的StringIO是类似的，但是和它唯一的不同就是，这个读取的是二进制数据
# 1 是直接将数据写入该对象中
b = BytesIO()
b.write('中文'.encode('UTF-8'))
print(b.getvalue())
# 2 就是在初始化对象的时候写入
b_test = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(b_test.read().decode('UTF-8'))

