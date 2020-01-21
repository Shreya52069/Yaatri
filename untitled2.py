# -*- coding: utf-8 -*-
"""
Created on Mon May 20 15:17:32 2019

@author: Shreya Bhardwaj
"""

from bs4 import BeautifulSoup
import requests
import xlsxwriter
import html2json
import json
import requests 
from bs4 import BeautifulSoup
import csv
from abc import ABC, abstractmethod

class Review(ABC):
    def __init(self):
        self.review = ""
        
    def review(rev):
        pass
        
    @abstractmethod
    def kalsang(self):
        pass
    @abstractmethod
    def blackpepper(self):
        pass
    
    @abstactmethod
    def saltandcarving(self):
        pass
    @abstractmethod
    def eddies(self):
        pass
    @abstractmethod
    def zenpanda(self):
        pass
    @abstractmethod
    def barbequeNation(self):
        pass
    @abstractmethod
    def doondarbaar(self):
        pass
    @abstractmethod
    def piccolo(self):
        pass

class reviewimplementation(Review):
    def kalsang(self):
        URL ="https://www.tripadvisor.in/Restaurant_Review-g297687-d4688102-Reviews-Kalsang_Friend_s_Corner-Dehradun_Dehradun_District_Uttarakhand.html"
        r = requests.get(URL)
        soup = BeautifulSoup(r.text, 'html.parser')
        #impdata = soup.find_all('<div class="wrap"></div>')
        da = soup.select(".wrap")
        kalfile = open('kalfile1.txt', 'a')
        for item in da:
            #print(item.text)
            textlist = item.text
            #print(type(textlist))
            print (textlist)
            fil.write(textlist)
        
