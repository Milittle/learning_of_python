# 当前线程的作用域
# 使用threading.local()获取这个对象
# 在线程中，最好的是使用局部变量，而不是使用全局全量
# 因为全局变量，线程在共享的时候必须加锁
# 所以引入下面的方式
import threading
local_thread = threading.local()
def print_student():
    print('current %s name is %s' % (threading.current_thread().name,local_thread.student))
def run_thread(name):
	local_thread.student = name
	print_student()
t1 = threading.Thread(target = run_thread,args = ('mi',))
t2 = threading.Thread(target = run_thread,args = ('guo',))
t1.start()
t2.start()
t1.join()
t2.join()

# 上面就是对于线程的局部值进行的一个存储
# 也就是在当前线程下面用的，这个值就只能在该线程下面获取