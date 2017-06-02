# 递归测试
# 阶乘递归求法
def fact(i):
    if i == 1:
        return 1
    return i * fact(i-1)
print(fact(5))

# 斐波那契数列递归求法
def fin(i):
    if i==0:
        return 0
    if i==1:
        return 1
    return fin(i-1)+fin(i-2)
print(fin(5))
# 汉诺塔递归求法
def han(n, a = 'A', b = 'B', c = 'C'):
    if n==1:
        print(a,'->',c)
        return None
    han(n-1, a, c, b)
    print(a, '->', c)
    han(n-1, b, a, c)
han(3)