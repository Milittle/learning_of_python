## 这里是介绍安装第三方模块的方法
# 这里需要python的一个pip安装管道程序
# window用户可以在安装python的时候点击add pip into path这个选项
# 其他的操作系统用户就不需要操心了，就直接进行一下的操作就好


## 下面是安装的步骤
# 1 一般来说，第三方的库都会在pypi.python.org这个网站上注册
# 2 需要知道这个第三方的库名字，可以在官网查询，后者上面这个网站查询是一样的
# 3 运行 pip install 库名字
# 4 比如处理图像的工具箱
# 5 pip install Pillow

from PIL import Image
im = Image.open('test.jpg')
print(im.format,im.size,im.mode)
im.thumbnail((500,500))
im.save('thumbmail.jpg')