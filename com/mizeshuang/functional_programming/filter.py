# python用于过滤用的函数filter()
# 与map函数和reduce函数类似，接受一个函数名和一个序列
# 与map不同的是filter函数是通过一个函数参数的True和False来判断是否返回该元素
# 当结果是True的时候才会返回到结果序列中
## 例如在一个list里面删除偶数，保留奇数
def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd,[1,2,4,5,6,9,10,15])))
# 结果是[1, 5, 9, 15]

## 将一个序列中的空字符串删除：

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['a','b',None,'','c'])))

# 由此可见，filter这个高阶函数旨在正确实现一个“筛选函数”
# 而且注意到filter函数返回的是一个Iterator对象，那么我们需要使用list()函数
# 返回一个list。

## 接下来使用这种方法来做寻求素数的程序
def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def not_divisible(n):
    return lambda x:x % n > 0
def primes():
    yield 2
    it = odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n),it)
## 打印1000以内的素数
for i in primes():
    if i < 1000:
        print(i)
    else:
        break