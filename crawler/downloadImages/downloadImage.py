from urllib.request import urlopen
from bs4 import BeautifulSoup

url = urlopen('http://kuas.ipv6.club.tw/~solomon/HTML/ch05_1_urlretrieve.html')
txt = url.read()
s = BeautifulSoup(txt, "lxml")
iamges = s.find_all("img")
for img in images:
  url = img.attrs["href"]
  file_name = img.string
  urllib.request.urlretrieve(url, file_name)