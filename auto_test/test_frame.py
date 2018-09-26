#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from ShowapiRequest import ShowapiRequest
from PIL import Image
import pytesseract
import time
import random

#print(EC.title_contains('注册'))
def send_keys():
	email_element=get_element_by_css('#register_email')
	usr_element=get_element_by_css('#register_nickname')
	pswd_element=get_element_by_css('#register_password')
	code_element=get_element_by_css('#captcha_code')
	'''
	email_element=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#register_email')))
	usr_element=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#register_nickname')))
	pswd_element=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#register_password')))
	code_element=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#captcha_code')))
	'''
	email_text=''.join(random.sample('012345abc',5))+'@163.com'
	usr_text=''.join(random.sample('012345abc',5))
	pswd_text=''.join(random.sample('012345abc_Ab',5))
	code_text=read_image()
	print(code_text)

	email_element.send_keys(email_text)
	usr_element.send_keys(usr_text)
	pswd_element.send_keys(pswd_text)
	code_element.send_keys(code_text)

def screen_shot():

	driver.save_screenshot(path+'/pic1.png')

def save_codeimg():
	iimg=Image.open(path+'/pic1.png')

	html = driver.find_element_by_tag_name("html")
	resize_width = html.size['width']
	resize_height = html.size['height']
	#print(image.get_attribute('title'))
	image=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#getcode_num')))
	left=image.location['x']
	top=image.location['y']
	right=image.location['x']+image.size['width']
	bottom=image.location['y']+image.size['height']
	resize_img = iimg.resize((resize_width, resize_height), Image.BILINEAR)
	#img=iimg.crop((left,top,right,bottom))
	img=resize_img.crop((left,top,right,bottom))
	img.save(path+'/pic11.png')
def read_image():
	screen_shot()
	save_codeimg()
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
	'''
	r = ShowapiRequest("http://route.showapi.com/184-5","62626","d61950be50dc4dbd9969f741b8e730f5" )
	r.addBodyPara("img_base64", "")
	r.addBodyPara("typeId", "35")
	r.addBodyPara("convert_to_jpg", "0")
	r.addBodyPara("needMorePrecise", "0")
	r.addFilePara("image", r"/Users/zhuo/Desktop/test/pic11.png") #文件上传时设置
	res = r.post()
	print(type(res)) # 返回信息
	#print(text)
	'''
def driver_init():
	driver.get('http://www.5itest.cn/register') 
	driver.maximize_window()
def get_element_by_css(css):
	return wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,css)))


if __name__ == '__main__':
	driver=webdriver.Chrome()
	wait=WebDriverWait(driver,5)
	path='/Users/zhuo/Documents/auto_test/image'
	driver_init()
	send_keys()
	submit_element=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#register-btn')))
	submit_element.click()
	
	#print(image.location)
	#print(image.size)
	time.sleep(10)
	driver.close()
	#driver.set_window_size(1440,900)

 


'''

'''


