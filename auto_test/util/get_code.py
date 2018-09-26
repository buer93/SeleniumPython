#coding=utf-8
from ShowapiRequest import ShowapiRequest
from PIL import Image
class GetCode():
	def __init__(self,driver):
		self.driver=driver
	def get_code_image(self,file_name):
		