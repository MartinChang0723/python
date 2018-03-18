import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.mis.kuas.edu.tw/main.php?mod=teacher&site_id=0')

# print ("%s" % r.text)

r.encoding = "UTF-8"

s = BeautifulSoup(r.text, "lxml")

tables = s.find_all("div", class_="itemContent")

for t in tables:
  name = t.find_all("tr")[0].find_all("td")[2].find("a").find("font").string
  name.encoding = 'UTF-8'

  mail = t.find_all("tr")[4].find_all("td")[1].find("a").string
  mail.encoding = 'UTF-8'

  print ("%s %s" % (name, mail))