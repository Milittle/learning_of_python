# 进程间通信问题
# 通常就是使用Queue、Pipes进行进程之间的通信
from multiprocessing import Process,Queue
import os,time,random
def write(q):
	print('Write process is running now(%s)' % (os.getpid()))
	for i in ['A','B','C']:
		print('Write %s into the queue' % (i))
		q.put(i)
		time.sleep(random.random())
def read(q):
	print('Read process is running now(%s)' % (os.getpid()))
	while True:
		value = q.get(True)
		print('Read %s into the queue' % (value))
if __name__ == '__main__':
	print('Father process is runnning(%s)' % (os.getpid()))
	q = Queue()
	pw = Process(target = write, args = (q,))
	pr = Process(target = read, args = (q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()