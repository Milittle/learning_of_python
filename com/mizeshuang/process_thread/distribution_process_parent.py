# 分布式
from multiprocessing.managers import BaseManager
import time,random,sys,queue
class QueueManager(BaseManager):
	pass

task_put = queue.Queue()
task_get = queue.Queue()

def return_put():
	global task_put
	return task_put
def return_get():
	global task_get
	return task_get
def test():
	QueueManager.register('get_task_put', callable = return_put)
	QueueManager.register('get_task_get', callable = return_get)
	manager = QueueManager(address = ('127.0.0.1',50000), authkey = b'abc')
	manager.start()
	t_put = manager.get_task_put()
	t_get = manager.get_task_get()
	for i in range(10):
		rand_int = random.randint(1,10000)
		print('put %s into the task_put' % (str(rand_int)))
		t_put.put(rand_int)
	for i in range(10):
		value = t_get.get(timeout = 10)
		print('get %s outo the task_get' % (str(value)))
	print('manager done!')

if __name__ =='__main__':
	test()