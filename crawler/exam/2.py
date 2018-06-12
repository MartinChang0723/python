from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import ssl 
import csv
context = ssl._create_unverified_context() 

url = urlopen('http://isin.twse.com.tw/isin/C_public.jsp?strMode=2', context=context)
txt = url.read()
s = BeautifulSoup(txt, "lxml")

# class name: field-name-field-dataset-resource
# target = s.findAll("div", {"class": "field-name-field-dataset-resource"})[0].find_all("div", {"class": "field-items"}).find_all("div", {"class": "field-item"})
print(s)
