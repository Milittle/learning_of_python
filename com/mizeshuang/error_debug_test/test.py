def fact(n):
	'''
	Simple test
	>>> fact(0)
	Traceback (most recent call last):
		...
	ValueError
	>>> fact(1)
	1
	>>> fact(2)
	2
	>>> fact(10)
	3628800
	'''
	if n < 1:
		raise ValueError()
	if n == 1:
		return 1
	else:
		return n * fact(n - 1)
# if __name__ == '__main__':
# 	import doctest
# 	doctest.testmod()

# 也可以使用python -m doctest test.py这样的方式进行测试