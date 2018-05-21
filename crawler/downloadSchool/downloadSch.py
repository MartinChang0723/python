from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import ssl 
import csv
context = ssl._create_unverified_context() 

url = urlopen('https://data.gov.tw/dataset/6091', context=context)
txt = url.read()
s = BeautifulSoup(txt, "lxml")

# class name: field-name-field-dataset-resource
# target = s.findAll("div", {"class": "field-name-field-dataset-resource"})[0].find_all("div", {"class": "field-items"}).find_all("div", {"class": "field-item"})
target = s.select('div.field-name-field-dataset-resource > div.field-items > div.field-item > div > a')
# print(target)
count = [0, 0, 0, 0, 0]
for tar in target:
  link = tar.attrs["href"]
  title = tar.string
  content = csv.reader(io.StringIO(urlopen(link).read().decode('utf-8')), delimiter=',')
  # print(content)
  # csv.reader()
  # content = io.StringIO(urlopen(link))
  for line in content:
    if line[2] == '公立':
      count[0] = count[0] + 1
    elif line[2] == '私立':
      count[1] = count[1] + 1
    if line[6] == '[1]一般':
      count[2] = count[2] + 1
    elif line[6] == '[2]技職':
      count[3] = count[3] + 1
    elif line[6] == '[3]師範':
      count[4] = count[4] + 1

print('公立', count[0])
print('私立', count[1])
print('[1]一般', count[2])
print('[2]技職', count[3])
print('[3]師範', count[4])
