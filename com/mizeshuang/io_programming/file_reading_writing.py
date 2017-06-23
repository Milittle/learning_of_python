# (1)读取文件的方式是用open函数进行文件的读写
# open(a,b) a 代表的是文件的路径，b 代表的是模式，r就是read、w就是write
try:
	f = open('./test.txt','r')
	file_string = f.read() # 可以读取文件中所有的内容到内存中，所以在文件大的情况下，不要一下都读到内存里
	print(file_string)
except IOError as e:
	print('Error: ', e)
else:
	print('no wrong')
finally:
	f.close() # 文件读取结束以后一定要进行文件流的关闭操作，不然会出错的
# 或者使用with语句就不需要进行关闭操作，因为with语句会为我们关系文件的
with open('./test.txt','r') as fp:
	print(fp.readline())

# 获取到文件流以后，就会对于怎么读这个文件的形式有三种方式
# 1 read()函数就是将所有的内容都读取到内存里面
# 2 readline()这个函数是读取第一行
# 3 readlines()这个函数是将文件的所有行读到一个list类型里面，也就是返回的是list类型

try:
	fl = open('./test.txt','r')
	for i in fl.readlines():
		print(i.strip()) # 这个strip函数是将末尾的'\n'去掉的
except IOError as e:
	raise IOError('read file is wrong!!!')
else:
	pass
finally:
	fl.close()

# file-like-object
# 这个一个类似于这个某个类，也就是在类继承的时候，子类可以就是像这个类而不一定要继承这个类才像这个类
# 这就是动态语言和静态语言的区别
# 在这里的话，就是说只要有read方法的就认为是流(不知道说的对不对，需要再思考)
# 除了 file 外，还可以是内存的字节流，网络流，自定义流等等
# StringIO 就是在内存中创建的 file-like Object，常用作临时缓冲。

# 二进制文件的读取，通常r的模式就是以UTF-8的形式直接读取文件
# 然而要是读取图片和视频等二进制信息的话，就需要使用rb模式
# 让我们来读取一个二进制的美女吧
with open('./beauty.jpg','rb') as beauty:
	print(beauty.readline())

# 带入字符编码的dict参数encoding
with open('./gbk.txt', 'r', encoding = 'gbk') as f:
	print(f.read())

# 如果读取的文件的时候会有一些错误的编码，可以进行忽略就是加参数errors='ignore'

with open('./gbk.txt','r', encoding = 'gbk', errors = 'ignore') as fig:
	print(fig.read())


# 写入文件的方式是就是用open函数，但是是用w的模式进行读取
# 在写文件和读取文件的时候一定要进行close操作，不然io会出问题的
with open('./write.txt','a') as fw:
	fw.write('hello world\r\n')