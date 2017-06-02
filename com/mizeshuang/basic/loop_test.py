names = ['mizeshuang', 'guojiaqi', 'shu', [1, 2, 3]]
for name in names:
    print(name)
# python里面提供了一个函数range(5)生成0-4的整数
a = list(range(5))
print(a)
s = 0
for x in range(101):
    s = s + x
print(s)

n = 100
k = 0
while n >= 0:
    k = k + n
    n = n - 1
print(k)
