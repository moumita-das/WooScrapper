import os
import urllib

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


print ("Enter category of search item")
search_item=input()
download_path = "flickr_downloads/"
if not os.path.exists(download_path):
			os.makedirs(download_path)
mainsite="https://www.flickr.com" ## main site from which we are gonna scrap
searchsite=mainsite+"/search/?text="+search_item.replace(" ", "%20")
urls=list()
for i in range(1): #No of reloads as flipkart diplays different cards in different requests
	urls.append(searchsite)
while len(urls)>0: #getting all the urls that are needed to be parsed
	browser = webdriver.Firefox()
	browser.get(urls[0])
	delay = 3
	WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, "overlay")))
	
	soup= BeautifulSoup(browser.page_source,"html.parser")
	urls.pop(0)
	images=[]
	count=0
	for tag in soup.findAll('a',{'class':'overlay'}):
		filename=search_item+str(count)
		src=mainsite+tag['href']+"/sizes/l"
		htmltext=urllib.request.urlopen(src).read()
		img_soup= BeautifulSoup(htmltext,"lxml")
		#img_soup=urllib.request.urlopen(src)
		img_src=img_soup.find('div',{'id':'allsizes-photo'}).find("img",{"src":True})		
		images.append(img_src['src'])
		
		
if not os.path.exists(download_path + search_item.replace(" ", "_")):
	os.makedirs(download_path + search_item.replace(" ", "_"))
folder_name=download_path + search_item.replace(" ", "_")
for image in images:
	print(os.system("wget "+image+" -P "+folder_name))
#print(images)

	
		
			

