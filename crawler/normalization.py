from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import sys

def main():
  if len(sys.argv) == 2:
    url = sys.argv[1]
  else:
    url = "http://KUAS.ipv6.club.tw/~solomon/a2.html"
  getLinks(url)

def getLinks(url):
  print(url)
  html = urlopen(url)
  bsObj = BeautifulSoup(html.read(), "html.parser")
  for tag in bsObj.findAll("a"):
    try:
      getLinks(tag.attrs["href"])
    except:
      getLinks(urljoin(url, tag.attrs["href"]))

main()