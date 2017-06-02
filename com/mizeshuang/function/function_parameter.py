# 函数参数
def my_pow(number,n=2):
    s = 1
    while n >= 1:
        s = s * number
        n = n - 1
    return s
print(my_pow(3,3))
s