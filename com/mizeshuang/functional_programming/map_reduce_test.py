from functools import reduce

def normalize(name):
    return str(name).title()
g = map(normalize,['adam', 'LISA', 'barT'])
for i in g:
    print(i)
def prod(x,y):
    return x * y
print(reduce(prod,[1,2,3,4,5]))

# 或者使用lambda表达式进行实现
print(reduce(lambda x,y:x * y,[1,2,3,4,5])) # 一行代码和上面的结果一样

def str2float(s):
    def char2num(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,}[s]
    def fn1(x,y):
        return x * 0.1 + y
    def fn2(x, y):
        return x * 10 + y
    s1 = s[0:s.find('.')]
    s2 = s[-1:s.find('.'):-1]
    print(s1,s2)
    return reduce(fn2,map(char2num,s1)) + reduce(fn1,map(char2num,s2)) * 0.1
print(str2float('123.456'))