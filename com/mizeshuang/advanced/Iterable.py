# 可以作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，分别有list、tuple、set、dict、str等
# 一类是generator，包括生成器和带yield的generator function
# 可以使用isinstance函数判断是否是一个Iterable对象
from collections import Iterable,Iterator
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance([x for x in range(10)],Iterable))
print(isinstance(100,Iterable))

# generator不但可以作用于for循环
# 而且还可以用next()函数进行作用，知道返回StopIteration
# 所以说generator也是一个Iterator
# 上面的list、tuple、set、dict、str虽然都用使用for循环进行迭代
# 只能说明是可迭代的，并不能说明是迭代器
# Iterator就是一个迭代器类型，generator就是一个Iterator
# 可以使用isinstance()函数进行判断是否为Iterator对象
print(isinstance([],Iterator))
print(isinstance('123',Iterator))
print(isinstance((),Iterator))
print(isinstance({},Iterator))
print(isinstance((x for x in range(10)),Iterator))
# 只有generator是Iterator，其他的都不是Iterator
# 要是要将list、tuple、set、str转换为Iterator
# 使用iter()函数就行
print(isinstance(iter([]),Iterator))
print(isinstance(iter('123'),Iterator))
print(isinstance(iter(()),Iterator))
print(isinstance(iter({}),Iterator))
