# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:44:39 2019

@author: Shreya Bhardwaj
"""

from bs4 import BeautifulSoup
import requests
class restaurants:
    #def __init():
        
     def fetch(self):
        url = "https://www.tripadvisor.in/Restaurants-g304551-New_Delhi_National_Capital_Territory_of_Delhi.html"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        da =soup.select(".poiTitle")
        file = open('E:/delhirestfile2', 'a')
        data = []
        for names in da:
             #textda = names.text
            data.append(names.text)
            print(names.text)
                    #print(data)
                    #dir(data)
        for item in data:
            file.write("%s\n" % item.encode('utf8'))
        file.close()
res = restaurants()
res.fetch()    
