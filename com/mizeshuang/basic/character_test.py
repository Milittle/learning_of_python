# 将A字母转换为对应的ascii码表示
print(ord('A'))
# 将 中 转换为对应的unicode码表示
print(ord('中'))
# 将对应的ascii码转换为字母B
print(chr(66))
# 将对应的unicode码用 文 表示
print(chr(25991))
# 效果和 中文 显示一样
print('\u4e2d\u6587')
# 将unicode编码的ABC转换为ascii码，相当于转换为bytes字节流
print('ABC'.encode('ascii'))
# 这个也是转换为字节流，只不过是utf-8
print('中'.encode('utf-8'))
# 将字节流的ABC转换为unicode编码
print(b'ABC'.decode('ascii'))
# 将字节流的中文转换为unicode编码
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf8'))
# 计算字符串的长度，默认计算的是字符串的长度，记住字符串在python里面是unicode。
print(len('ABC'))
print(len('中文'))
# 计算byte的长度
print(len('ABC'.encode('utf-8')))
print(len('中文'.encode('utf-8')))
