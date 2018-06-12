from requests_html import HTMLSession
from bs4 import BeautifulSoup
import ssl 
import csv
context = ssl._create_unverified_context()

session = HTMLSession()
r = session.get('http://wwwfile.megabank.com.tw/other/bulletin02_02.asp')
ht = r.html.render()
print(ht)
# s = BeautifulSoup(r, "lxml")
# target = s.select('#I > tbody')
# print (target)