# 多任务可以使用多进程的形式也可以使用多线程的形式
# python实现了_thread和threading两个模块供大家实现多线程
# 其实一般情况下threading就够了
import threading,time
def loop():
	print('thread %s is running' % (threading.current_thread().name))
	n = 0
	while n < 5:
		print('thread %s >>> %s' % (threading.current_thread().name,str(n)))
		n += 1
		time.sleep(0.1)
	print('thread %s is done!' % (threading.current_thread().name))
print('thread %s is running' % (threading.current_thread().name))
t = threading.Thread(target = loop,name = 'Loopthread') # 如果此处没有定义线程的名字的话，系统会自定义
t.start()
t.join()
print('thread %s is done!' % (threading.current_thread().name))

# 接下来有一个要注意的地方就是
# 线程相对于进程的资源是共享的
# 所以线程在访问统一资源的时候
# 这一资源必须上锁
# 这个锁是通过threading.Lock()获取的
# 我们下面写一个共享资源的例子
balance = 0
lock = threading.Lock()

def change_it(n):
	global balance # 必须声明是全局的balance，因为在函数中如果不定义为全局变量，在函数外无法访问
	balance += n
	balance -= n
def run_thread(n):
	for i in range(1000000): # 主要是运行次数多了，就会出现线程的共享资源出现问题
	    lock.acquire()
	    try:
		    change_it(n)
	    except Exception as e:
	    	raise e
	    else:
	    	pass
	    finally:
	    	lock.release()

th1 = threading.Thread(target = run_thread, args = (8,))
th2 = threading.Thread(target = run_thread, args = (-1,))
th1.start()
th2.start()
th1.join()
th2.join()
print(balance)


# 那我们为了避免上面的情况发生，我们需要给run_thread这个函数上锁
# 上了所以后就不会出现错误了
# 但是上了锁以后速度就会明显的减慢
# 而且在多线程模式中，如果多个线程访问多处共享资源的时候同时上锁
# 那么造成的后果就是，这几个线程会成为死锁
# 这样所有的线程将无法执行
# 只能通过操作系统自行终止



# 在python中，就不断启动多少个线程，都不会所有的核都用上，因为在python中
# 一个进程有一个全局的Global Interpreter Lock
# python的所有程序在执行程序的hi收必须要获得这个锁
# 这个全局锁会控制所有线程没执行一段代码以后就释放这个锁
# 所以在python中实现多线程利用多核的任务不会实现
# 所以我们用多进程可以实现这个功能
# 
