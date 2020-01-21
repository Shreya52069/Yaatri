# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:19:14 2019

@author: Shreya Bhardwaj
"""

from bs4 import BeautifulSoup
import requests
class adventureplaces:
    #def __init():
        
     def fetch(self):
         
        url = "https://www.thrillophilia.com/adventure-sports-in-delhi"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        data =soup.select(".clickable-image")
        #print(data)
        uniq_list=[]
        for names in data:
            attr=names.attrs
            uniq_list.append(attr['alt'])
        uniq_list = list(set(uniq_list))
        #print(uniq_list)
        file = open('E:/adventurefile5', 'a')
        for names in uniq_list:
            file.write("%s\n" % names.encode('utf8'))
        file.close()
res = adventureplaces()
res.fetch()    
