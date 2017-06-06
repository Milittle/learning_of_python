## 排序函数的说明
print(sorted([-1,2,5,-78,56]))
## 以上的是对序列直接进行升序排列
print(sorted([-1,2,5,-78,56],key=abs))
## 以上是对序列经过key函数的作用以后进行升序排列
print(sorted([-1,2,5,-78,56],key=abs,reverse=True))
## 以上是对
print(sorted(['a','Zoo','bob','about','Credit']))
print(sorted(['a','Zoo','bob','about','Credit'],key = str.lower))
print(sorted(['a','Zoo','bob','about','Credit'],key = str.lower,reverse=True))

### 最后sorted函数也是一个高阶函数，用sorted函数的排序关键在于实现一个映射函数


## 练习

def by_grades(t):
    return t[1]

def by_name(t):
    return t[0]
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L,key = by_name))
print(sorted(L,key = by_grades,reverse=True))