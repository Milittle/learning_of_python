# 正则表达式
# \d 是数字的表示
# \w 是字母的表示
# \s 是空格的表示
# . 是匹配任意字符的表示
# [a-z] 可选的表示 这个表示是a-z的字母随便匹配
# () 分组，这是在python中匹配的时候可以将待匹配字符串进行分组，最后可以返回一个list
# * 表示0以上包含0
# + 表示1以上包含1
# ？表示0或者1
# {n,m} 表示n-m个
# | 表示或者的意思
# ^ 表示匹配开头
# $ 表示匹配结尾
# python中有re模块可以进行编程
# 一般为了避免和python内部的转义字符\冲突，我们一般在re字符串前面加上r这样说明是正则表达式
import re
group = re.match(r'(\d{3})-(\d{5})','020-12345').groups()  # match函数返回一个Match对象，groups函数返回一个tuple对象
print(group)

lst = re.split(r'[\s\,\;]+','a,, b;c ,d') # split函数返回一个list
print(lst)

# 最后就是强调一下，re是贪婪匹配
# 为了让它消失这个贪婪匹配，我们需要在后面加上？
# 实例展示

print(re.match('^(\d+)(0*)$', '12300').groups())
print(re.match('(\d+?)(0*)', '12300').groups())

