## 这个偏函数不是数学界的那个偏函数的定义
# 这个偏函数的定义就是让一些函数的默认参数得到确认
# 进行二次定义该函数
## 比如int这个函数后面有一个参数是base参数，这个参数决定了可以处理几进制的字符串对象
## 那么我们可以直接定义这样的函数
## such as
from functools import partial
int2 = partial(int,base = 2)
# 那么现在的int2函数就是输出二进制的数
print(int2('1100'))

## 在创建偏函数的时候
# 其实是可以传入函数，*args，**kwargs这三个参数的
# 比如上面的函数就是传入的是**kwargs这个参数的
k = {'base':2}
print(int('11001100',**k))
## 比如传入这个参数的时候就是传入的是*args这个参数并加在了左边
max2 = partial(max,10)
print(max2(1,2,3,4,5,6))
