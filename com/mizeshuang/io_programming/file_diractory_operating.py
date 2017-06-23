# 使用python操作系统文件和目录
# 使用python的os模块提供的函数操作这些文件和目录
import os
print(os.name) #如果是 posix，说明系统是 Linux、Unix 或 Mac OS X，如果是 nt，就是 Windows 系统。
# 需要详细的信息的话直接调用os的uname()函数
# print(os.uname()) # 注意 uname()函数在 Windows 上不提供，也就是说，os 模块的某些函数是跟操作系统相关的。


# 1 环境变量
# 在操作系统中存的变量都是放在os.environ这个变量里面的
print(os.environ)
# 需要获取特定的环境变量使用以下方式进行
print(os.environ.get('JAVA_HOME')) # C:\Program Files\Java\jdk1.8.0_101

# 2 操作目录和文件：都是房子啊os模块和os.path模块里面的
# 2.1 操作目录
print(os.path.abspath('.')) #查看当前目录绝对路径
# C:\Users\mizes\PycharmProjects\learning_of_python\com\mizeshuang\io_programming
# 在某个目录下面创建新的目录,首先将目录路径连接在一起，或者也可以不连接，直接进行创建
dir = os.path.join('.','milittle')
# 创建文件夹
# os.mkdir(dir)
# 删除文件夹
# os.rmdir(dir)

# 上面使用os.path.join()函数是因为根据不同的操作系统，就能分别构造不同的分隔符
# 因为在linux里面是'/'这个样子的分隔符，在Windows上是'\'这样的分隔符
# 同理在拆分路径的时候就用os.path.split()
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
print(os.path.split('/Users/milittle/testdir')) # 分离最后以及目录或者文件和最前面的目录
print(os.path.splitext('/Users/milittle/testdir/test.apg.txt')) # 这个是将文件的后缀提取出来的,当没有文件的时候就返回''
# 2.2对文件的操作
# 对文件的重命名
# os.rename('./rename','rename')
# 对文件进行的删除
# os.remove('./del')
# 但是在os模块里面没有赋值文件的函数
# 那么这个操作在shutil模块提供了copyfile()
import shutil
goal = os.path.join('d:','copy.txt')
shutil.copyfile('./rename',goal) # 这个就将当前文件夹里面的rename文件拷贝到你的d盘下面了

# 下面用实例来展示
# 列出该文件夹下面的所有的目录
# print([x for x in os.path.lisdir('.') if os.path.isdir(x)]) # 这个函数在window上面不支持
# print([x for x in os.path.listdir(.) if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

# 要知道，在python里面，操作文件和目录的函数都在os和os.path模块里面呢
# 但是有的函数在不同的操作系统下才可以执行
# 还有就是在shutil模块里面有一个拷贝文件的函数copyfile函数
