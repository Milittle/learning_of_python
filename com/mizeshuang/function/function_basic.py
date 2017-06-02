# 这是函数的基础
# 因为函数的就是对重复问题的解决
# 比如从1加到100
def my_sum(a):
    s=None
    while a >= 0:
       s = s+a;
       a = a-1
    return s
print(my_sum(-1))

