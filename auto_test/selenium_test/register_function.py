#coding=utf-8
import sys
sys.path.append('/Users/zhuo/Documents/auto_test')
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from ShowapiRequest import ShowapiRequest
from PIL import Image
import pytesseract
import time
import random
from find_element import FindElement

class RegisterFunction(object):
	"""docstring for RegisterFunction"""
	def __init__(self,url):
		self.driver=self.get_driver(url)
	#获取driver并且打开URL
	def get_driver(self,url):
		driver=webdriver.Chrome()
		driver.get(url)
		#driver.maxmize_window()
		return driver  
	#输入用户信息
	def send_user_info(self,key,data):
		self.get_usr_element(key).send_keys(data)


	#定位用户信息，获取element
	def get_usr_element(self,key):
		find_element=FindElement(self.driver)
		usr_element=find_element.get_element(key)
		return usr_element
	#屏幕截图
	def screen_shot(self):
		self.driver.save_screenshot(path+'/pic1.png')
	#获取验证码截图
	def save_codeimg(self):
		iimg=Image.open(path+'/pic1.png')

		html = self.driver.find_element_by_tag_name("html")
		resize_width = html.size['width']
		resize_height = html.size['height']
		#print(image.get_attribute('title'))
		#image=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#getcode_num')))
		image=self.get_usr_element('code_image')
		left=image.location['x']
		top=image.location['y']
		right=image.location['x']+image.size['width']
		bottom=image.location['y']+image.size['height']
		resize_img = iimg.resize((resize_width, resize_height), Image.BILINEAR)
		#img=iimg.crop((left,top,right,bottom))
		img=resize_img.crop((left,top,right,bottom))
		img.save(path+'/pic11.png')
	def get_random(self):
		return random.sample('123456abc',5)
	#读取验证码信息
	def read_image(self):
		self.screen_shot()
		self.save_codeimg()
		i=Image.open(path+'/pic11.png')
		#text=pytesseract.image_to_string(i)
		#from ShowapiRequest import ShowapiRequest
		r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
		r.addBodyPara("typeId", "35")
		r.addBodyPara("convert_to_jpg", "0")
		file_name=path+'/pic11.png'
		r.addFilePara("image", file_name) #文件上传时设置
		res = r.post()
		#text = res.json()['showapi_res_body']['Result']
		return res.json()['showapi_res_body']['Result']# 返回信息
	def main(self):
		driver=self.get_driver(url)
		self.send_user_info('user_email',''.join(self.get_random())+'@163.com')
		self.send_user_info('user_name',''.join(self.get_random()))
		self.send_user_info('password',''.join(self.get_random()))
		text=self.read_image()
		self.send_user_info('code_text',text)
		self.get_usr_element('register_button').click()
		if self.get_usr_element('code_text_error'):
			print('注册成功')
		else:
			print('注册失败')  
			self.driver.save_screenshot(path+'/codeerror.png')
		self.driver.close()
		
if __name__ == '__main__':
	url='http://www.5itest.cn/register'
	path='/Users/zhuo/Documents/auto_test/image'
	test=RegisterFunction(url)
	test.main()
	

		