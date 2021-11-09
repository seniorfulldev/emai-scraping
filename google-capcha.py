from io import BytesIO 
import lxml.html 
from PIL import Image 
import urllib.request 
import re
from bs4 import BeautifulSoup
def load_captcha(html): 
   tree = lxml.html.fromstring(html) 
   img_data = tree.cssselect('div#recaptcha img')[0].get('src') 
   img_data = img_data.partition(',')[-1] 
   binary_img_data = img_data.decode('base64') 
   file_like = BytesIO(binary_img_data) 
   img = Image.open(file_like) 
   return img 


url = "https://www.upwork.com"
page = urllib.request.urlopen(url) 

soup = BeautifulSoup(page,features='html.parser')
load_captcha(soup)