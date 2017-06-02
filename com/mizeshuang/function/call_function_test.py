# 调用函数测试
print(abs(-100))
# print(abs('mi'))## 会提示TypeError错误提示
print(max(1,2,3,4,5,67,8))
# 数据类型转化的函数
print(int('1'))
print(float('1.23'))
print(str(123))
print(bool(''))

# 牢记一点就是，函数只不过是指向函数的一个引用而已，完全可以吧函数名赋值给一个变量，这样就可以使用这个变量调用函数了
int_function=int
print(int_function('123456'))

# 将一个整数转换为十六进制字符串表示
print(str(hex(255)).encode('utf-8').decode('utf-8').encode('utf-8'))
