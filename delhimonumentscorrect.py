# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:19:09 2019

@author: Shreya Bhardwaj
"""

from bs4 import BeautifulSoup
import requests
class monuments:
    #def __init():
        
     def fetch(self):
            url = "https://www.ixigo.com/monuments-in-of-around-near-new-delhi-lp-1140454"
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            da =soup.select(".ne-title")
             #print(da)
            file = open('E:/monumentsfile16', 'a')
            
            for names in da:
                
                #print(names.text)
                file.write("%s\n" % names.text.strip().encode('utf-8'))
            
            file.close()
            
res = monuments()
res.fetch()    
