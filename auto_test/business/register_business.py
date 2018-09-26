#coding=utf-8
from handle.register_handle import RegisterHandle
class RegisterBusiness(object):
	#执行操作
	def __init__(self,driver):
		self.register_h=RegisterHandle(driver)
	def user_base(self,email,name,password,code):
		self.register_h.send_email(email)
		self.register_h.send_user_name(name)
		self.register_h.send_password(password)
		self.register_h.send_code_text(code)
		self.register_h.click_register_button()
	#登陆成功
	def login_success(self,email,name,password,code):
		self.user_base(email,name,password,code)
		
		if self.register_h.get_register_text() ==None:
			return True
		else: 
			print('检验成功')
			return True

	#邮箱错误
	def login_email_error(self,email,name,password,filename):
		self.user_base(email,name,password,filename)
		pass
		'''
		if self.register_h.get_user_text('email_error','请输入有效的电子邮件') == None：
			#print('邮箱校验成功')
			return True
		else: 
			return False
		'''
	#用户名错误
	def login_name_error(self,email,name,password,filename):
		self.user_base(email,name,password,fielname)
		if self.register_h.get_user_text('name_error','')==None:
			#print('邮箱校验成功')
			return True
		else: 
			return False
		
	#密码错误
	def login_password_error(self,email,name,password,filename):
		self.user_base(email,name,password,filename)
		if self.register_h.get_user_text('password_error','')==None:
			#print('邮箱校验成功')
			return True
		else: 
			return False

	#验证码错误
	def login_code_error(self,email,name,password,filename):
		self.user_base(email,name,password,filename)
		if self.register_h.get_user_text('code_error','')==None:
			#print('邮箱校验成功')
			return True
		else: 
			return False

	
