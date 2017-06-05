# 在python中一边循环一遍计算的机制就叫做生成器:generator
# 要创建一个generator，有很多中办法，第一种办法很简单，只要把列表生成式中的[]换成()，就可以创建一个generator了
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print (g)
# 创建L和g的区别就是在于最外层的[]和(),L是一个list，而g是一个generator
# 我们可以直接打印出L的元素，但是g的元素不能直接打印，只能通过next()函数进行打印
# 但是一般是不会使用next()方法进行打印的，因为调用最后会产生stopInteration错误只是通过for循环进行访问的
for n in g:
    print (n)
# 生成器还有很大的用法
# 比如下面的斐波那契数列，普通的改为generator的写法
# general
def fib(x):
    n,a,b = 0,0,1
    while n < x:
        print (b)
        a,b = b,a + b
        n = n + 1
    return 'done'
print(fib(6))

def fib_gen(x):
    n,a,b = 0,0,1
    while n < x:
        yield b
        a,b = b,a + b
        n = n + 1
    return 'done'
fib_g = fib_gen(6)
print(fib_g)

for x in fib_g:
    print(x)
