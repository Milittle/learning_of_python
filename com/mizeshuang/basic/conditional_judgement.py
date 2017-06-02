a = 5
if a >= 18:
    print('you age is %d' % a)
    print('you are adult')
elif a >= 6:
    print('you are teenager')
else:
    print('you are kid')

# if的条件可以是简写的，如果是非零数值、非空字符串、非空list等，就判断为True，否则为false
# 再议input函数，因为input函数读取进去的数据都是str，所以要是整数的话，那么需要使用int函数进行转换
a = input("input a number")
b = int(a)
if b >= 10:
    print("this number is more than 10")
else:
    print("this number is less than 10")


