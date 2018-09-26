#coding=utf-8
import sys
sys.path.append('/Users/zhuo/Documents/auto_test')
from business.register_business import RegisterBusiness
from selenium import webdriver
import unittest
import HTMLTestRunner
import os
class FristCase(unittest.TestCase):
	'''
	def __init__(self):
		self.driver=webdriver.Chrome()
		self.driver.get('http://www.5itest.cn/register')
		self.login=RegisterBusiness(self.driver)
	'''
	@classmethod
	def setUpClass(self):
		self.file_name=''

		print('所有case执行前')
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.get('http://www.5itest.cn/register')
		self.login=RegisterBusiness(self.driver)
			def tearDown(self):
		print('这是case的后置条件')
		for method_name,error in self._outcome.errors:
			if error:
				case_name=self._testMethodName
				file_path=os.path.join(os.path.dirname(os.getcwd())+'/report/'+case_name+'.png')

				case_
				self.driver.save_screenshot()

		self.driver.close()
	
    #邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
	'''
	def test_login_email_error(self):
		email_error = self.login.login_email_error('1314@qq.com','user1111@qq.com','111111','0000')
		#return self.assertFalse(email_error,"测试失败")
	''' 
	def test_login_username_error(self):
		username_error = self.login.login_name_error('12123@qq.com','t1','111111','0000')
		self.assertTrue(username_error,'ca')

	def test_login_code_error(self):
		code_error = self.login.login_name_error('11121@qq.com','ss22212','111111','0000')
		self.assertFalse(code_error)
    
	def test_login_password_error(self):
		password_error = self.login.login_name_error('11311@qq.com','ss23222','111111','0000')
		self.assertFalse(password_error)

	def test_login_success(self):
		success = self.login.user_base('12221@qq.com','2321','111111','0000')
		print(success)
		self.assertFalse(success)
'''	
def main():
	first=FristCase()
	first.test_login_success()
	#first.test_login_email_error()
	first.test_login_username_error()
	first.test_login_password_error()
	first.test_login_code_error()
'''
if __name__=="__main__":
	file_path=os.path.join(os.path.dirname(os.getcwd())+'/report/'+'first_case.html')

	print(file_path)
	f=open(file_path,'wb')
	suite=unittest.TestSuite()
	suite.addTest(FristCase('test_login_username_error'))
	unittest.main()
	runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='this is first report',description='这是我们第一次测试报告',verbosity=2)
	runner.run(suite)


	#main()
