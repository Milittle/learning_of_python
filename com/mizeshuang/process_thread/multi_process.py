# 多进程模式编程
# 理解了linux里面的fork函数就可以对多进程有一个很好的理解
# 在python中是有os模块来干这件事情的
import os
print('Process (%s) start...' % os.getpid())

# 下面的进程调用是在linux/unix/Mac
# pid = os.fork() # 这个函数返回两次，第一次返回给主进程，返回的是子进程的pid，第二次给子进程返回，返回时零
# if pid == 0:
# 	print('i am a child (%s) my father is (%s)' % (os.getpid(),os.getppid()))
# else:
# 	print('i am a father (%s) my child is (%s)' % (os.getpid(),pid))
# Process (2320) start...
# I (2320) just created a child process (2321).
# I am child process (2321) and my parent is 2320.

# 那么在windows上面可以使用mutiprocessing这个模块来编写多进程程序

from multiprocessing import Process

def run_child(arg):
	print('i am child %s (%s), begining to run' % (arg, os.getpid()))

if __name__ == '__main__':
    print('i am father (%s)' % os.getpid)
    p = Process(target = run_child,args = ('test_child',))
    print('child will start')
    p.start()
    p.join()
    print('child end')
# Process (8908) start...
# i am father (<built-in function getpid>)
# child will start
# Process (12016) start...
# i am child test_child (12016), begining to run
# child end


# 创建子进程时，只需要传入一个执行函数和函数的参数，
# 就类似于c++的执行方式
# target = function, args = (参数,) # 这个args是一个tuple
# 创建一个 Process 实例，用 start()方法启动，这样创建进程
# 比 fork()还要简单。
# 据我做的实验，这个windows上面子进程是无法获取到父进程的pid的

# 下面是创建很多个子进程的时候使用Pool来做支持

from multiprocessing import Pool
import os, time, random

def multi_process(n):
	print('Run task number is (%s)' % (n))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('task %s run %0.2f seconds.' % (name, (end - start)))
if __name__ == '__main__':
	print('parent process is (%s)' % (os.getpid))
	p = Pool(4)
	for i in range(5):
		p.apply_async(multi_process, args = (i,))
	print('wait all sun_process execute end')
	p.close()
	p.join()
	print('ALL sun_process aleardy have executed end')

