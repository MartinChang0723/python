import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.csie.ncnu.edu.tw/Default.aspx?CID=17')

# print ("%s" % r.text)
#Content > table > tbody > tr:nth-child(2) > td:nth-child(2) > font > a:nth-child(5)
r.encoding = "UTF-8"

s = BeautifulSoup(r.text, "html5lib")

# print (s)

tables = s.find_all("td", {"valign": "middle"})

# print(tables)

for t in tables:
  if len(t.find("font").find_all("a")) < 2:
    name = t.find("font").contents[0]
    mail = t.find("font").contents[7].string
    name.encoding = 'UTF-8'
    mail.encoding = 'UTF-8'
    print(t.find("font").string)
    print ("%s %s" % (name, mail))
  else:
    name = t.find("font").find_all("a")[0].string
    name.encoding = 'UTF-8'

    mail = t.find("font").find_all("a")[1].string
    mail.encoding = 'UTF-8'

    print ("%s %s" % (name, mail))