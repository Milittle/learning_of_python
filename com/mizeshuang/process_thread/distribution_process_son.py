from multiprocessing.managers import BaseManager
import time, queue
class QueueManager(BaseManager):
	"""docstring for QueueManager"""
	pass

QueueManager.register('get_task_put')
QueueManager.register('get_task_get')

manager = QueueManager(address = ('127.0.0.1', 50000), authkey = b'abc')

manager.connect()

put = manager.get_task_put()
get = manager.get_task_get()

for i in range(10):
	value = put.get(timeout = 0)
	print('calculate %s * %s' %(str(value),str(value)))
	get.put(value * value)
