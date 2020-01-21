# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:48:24 2019

@author: 500052069
"""
import requests 
from bs4 import BeautifulSoup
class shopping:
    #def __init():
        
     def fetch(self):
        
         url = "https://www.travelogyindia.com/delhi/shopping-in-delhi.html"
         r = requests.get(url)
         soup = BeautifulSoup(r.text, 'html.parser')
         data =soup.select(".guide-inner-list")
         file = open('E:/shoppingfile6', 'a')
         shopdata = []
         for names in data:
            
            shopdata.append(names.text)
            #print(names.text)
        #print(data)
        #dir(data)
         for item in shopdata:
            file.write("%s\n" % item.encode('utf8'))
         file.close()
res = shopping()
res.fetch()    
