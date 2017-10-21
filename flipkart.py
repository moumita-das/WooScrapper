import os
import urllib
import csv
from bs4 import BeautifulSoup
mainsite="https://www.flipkart.com/" ## main site from which we are gonna scrap
urls=list()
for i in range(5): #No of reloads as flipkart diplays different cards in different requests
	urls.append(mainsite)
name=list()
price=list()
off=list()
while len(urls)>0: #getting all the urls that are needed to be parsed
	htmltext=urllib.request.urlopen(urls[0]).read()
	soup= BeautifulSoup(htmltext,"lxml")
	urls.pop(0)
	for tag in soup.find('div',{'class': '_2NTrR2'}).findAll('div',{'class':'_2kSfQ4'}):
		if tag.find('div',{'class': 'iUmrbN'}) not in name:
			name.append(tag.find('div',{'class': 'iUmrbN'}))
			price.append(tag.find('div',{'class': 'BXlZdc'}))
			off.append(tag.find('div',{'class': '_3o3r66'}))
for i in range(len(name)):
	print(name[i].text+"----"+price[i].text+"----"+off[i].text)
