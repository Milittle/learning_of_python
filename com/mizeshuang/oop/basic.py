## 在python中所有的数据类型都是对象，当然也可以自定义对象
# 这和java的一切皆对象的理论有的一拼
## 例如我们需要存储一个学生的名字和成绩信息
# 我们可以使用dict对象进行存储
student1 = {'name':'mizeshuang','score':98}
student2 = {'name':'guojiaqi','score':100}
def print_score(std):
    print('%s,%s' % (std['name'],std['score']))
print_score(student1)

## 上面是面向过程的解法
# 一般面向对象的编程思想就是
# 将一个事物抽象成一个整体，里面包含什么数据，就是里面具有的数据
# 再就是这个事物具有什么样的功能，可以进行什么样的操作


## 例如下面的Student类
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s,%s'%(self.name,self.score))
std1 = Student('mizeshuang',100)
std1.print_score()

## 对象是实例的抽象
# 实例是对象的具体对象