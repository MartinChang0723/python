from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import ssl 
import csv
context = ssl._create_unverified_context() 

url = urlopen('http://www.books.com.tw/activity/gold66_day/?loc=P_021_1_more_001', context=context)
txt = url.read()
s = BeautifulSoup(txt, "lxml")

# class name: field-name-field-dataset-resource
# target = s.findAll("div", {"class": "field-name-field-dataset-resource"})[0].find_all("div", {"class": "field-items"}).find_all("div", {"class": "field-item"})
target = s.select('#week')

for dii in target[0].find_all('div'):
  try:
    if len((dii.attrs['class'])) == 1:
      if len(dii.attrs['class'][0]) == 6:
        date = dii.select('.day')[0].string
        name = dii.select('div.sec_day > div > h1 > a')[0].string
        h2s = dii.select('div.sec_day > div > h2')
        provider = h2s[0].contents[0] + h2s[0].contents[1].string
        price = h2s[1].string
        newPrice = h2s[2].contents[0] + h2s[2].contents[1].string + h2s[2].contents[2]
        print (date)
        print (name)
        print (provider)
        print (price)
        print (newPrice)
        print ('\n')
  except:
    pass

