#coding=utf-8
import unittest
class FirstCase01(unittest.TestCase):
	"""docstring fss FirstCase01"""
	
		
	@classmethod
	def setUpClass(cls):
		print('所有case的前置条件')
	@classmethod
	def tearDownClass(cls):
		print('所有case的后置条件')
	def setUp(self):
		print('这个是case的前置条件')
	def tearDown(self):
		print('这个是case的后置条件')
	@unittest.skip('不执行第一条')
	def testfirst01(self):
		print('这是第一条case')
	def testfirst02(self):
		print('这是第二条case')
	def testfirst03(self):
		print('这是第三条case')

if __name__=='__main__':
	#unittest.main()
	'''
	suite=unittest.TestSuite()
	suite.addTest(FirstCase01('testfirst02'))
	unittest.TextTestRunner().run(suite)
	'''
