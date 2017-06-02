# list是python里面的内置数据类型，是一个有序集合，可以随时添加删除其中的元素
# 定义
classmates = ['mizeshuang','guojiaqi','zhangwang']
print(classmates)
# 可以使用len函数计算list的长度
le = len(classmates)
print('classmats的长度:%d' % le)
# 用索引访问list中每一个位置的元素，记得元素的索引从0开始
# 比如下面你的例子
print(classmates[0])
# 特殊的地方就是list可以支持负数的索引，也就是len()的长度加那个负数就是当前索引的位置
print(classmates[-1])
# list是一个可变的有序列表，它可以往后面追加元素
classmates.append('chenruiqing')
print(classmates)
# list也可以进行插入操作
classmates.insert(1,'lijinyang')
print(classmates)
# list也可以进行删除操作，删除末尾的一个元素
classmates.pop()
print(classmates)
# list要删除指定位置的元素，需要在pop函数里面加上索引
classmates.pop(1)
print(classmates)
# list要想替换某个元素，直接对索引位置的元素进行赋值替换操作即可
classmates[1]='lijinyang'
print(classmates)
# list里面的元素可以不一样，例如下面的例子
s = ['apple', True, 123]
print(s)
# list里面还可以包含另一个list，例如下面的例子
d = ['mi', [123, 456], True]
print(d)
print(d[1][1])  # 相当于二位数组matrices
# 或者直接用变量代替
q = [123, 456, 789]
p = ['sure', 'thanks', q, True]
print(p)
# 如果是一个空list的话，那么长度就是0
print(len([]))



# tuple与list有点相似，但是最大的不通就是tuple一初始化，就不能进行修改操作
# 这个不能改变的对象就是里面的元素不能进行改变
# 还有就是，tuple在定义的时候，就必须确定下来
# tuple也没有有append方法和insert方法
# tuple也可以使用负数索引的方式进行访问操作
# 但是就是如果在初始化tuple的时候，如果是一个元素的话，那么在括号里面的数字后面加上一个逗号
# 不然的话，解释器就会认为这是一个带有括号的数字而已
# 就不会当作一个元组来处理
t = (1, 2)
print(t)
f = (8, )
print(f)
# 还有重要的一个点，就是tuple自身的指向不能发生改变，但是它里面如果还有list的话，这个list的内容是可以改变的
