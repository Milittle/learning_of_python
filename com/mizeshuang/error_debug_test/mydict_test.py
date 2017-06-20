#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import unittest
from unit_test import MyDict
class TestDict(unittest.TestCase):
	def setUp(self):
		print('setUp...')
	def tearDown(self):
		print('tearDown...')
	def test_init(self):
		d = MyDict(a = 1, b = 'test')
		self.assertEqual(d.a,1)
		self.assertEqual(d.b,'test')
		self.assertTrue(isinstance(d,dict))
	def test_key(self):
		d = MyDict()
		d['key'] = 'value'
		self.assertEqual(d.key, 'value')
	def test_attr(self):
		d =MyDict()
		d['key'] = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d.key, 'value')
	def test_keyerror(self):
		d = MyDict()
		with self.assertRaises(KeyError): # 这里的意思就是期待抛出这个异常，所以检测是正确的
			value = d['empty'] # 我的理解就是在不出现这个key的时候就会抛出keyError这个类型的错误
	def test_attrerror(self):
		d = MyDict()
		with self.assertRaises(AttributeError): # 这里的意思就是期待抛出这个异常，所以检测是正确的
			value = d.empty # 这个类似，就是没有这个属性的时候抛出AttributeError
# 在编写这个类的时候，我们首先继承了unittest.TestCase这个类
# 在这个类里面的所有以test开头的方法都是测试方法
# if __name__ == '__main__':
# 	unittest.main()
# 上面这种方法可以进行测试代码的执行，这个就是可以直接运行的代码
# 还有一种方法就是在后面加上-m unittest 这个参数运行单元测试
# 测试结果如下：
# .....
# ----------------------------------------------------------------------
# Ran 5 tests in 0.001s

# OK

# setUp() 和 tearDown()
# 这两个方法是在每个测试方法前后运行的，setUp运行在测试函数前面
# tearDown运行在测试函数后面