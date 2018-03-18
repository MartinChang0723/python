import re
import requests
from bs4 import BeautifulSoup

r = requests.get('http://en.ncnu.edu.tw/index.php?option=com_content&view=article&id=283&Itemid=437')

# print ("%s" % r.text)

r.encoding = "UTF-8"

s = BeautifulSoup(r.text, "html5lib")

# print (s)

aaa = s.find_all(href=True)

# print (aaa)

for aa in aaa:
  if re.match("http", aa.get('href')):
    print (aa.get('href'))