# 定义函数关键字def
def my_abs(i):
    if i >0:
        return i
    else:
        return -i
print(my_abs(123))
# 空函数,使用pass将函数代码去填充，这样程序就可以执行，后续可以补上代码
def nop():
    pass

# 参数检查
# 当参数数目不对的时候，python的编译器会给我们检测出来
# 但是参数类型出现了问题，就不会检查
# 所以需要程序员自己检查
def my_abs_plus(i):
    if not isinstance(i,(int,float)):
        raise TypeError('bad operand type')
    if i >=0:
        return i
    else:
        return -i
print(my_abs_plus(-100))
## print(my_abs_plus('mi'))
# 返回多个值,返回的值是tuple
def return_more_value():
    return 1,2,3
print(return_more_value())