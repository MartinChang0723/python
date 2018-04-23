import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

f = open("rainfall.csv","w")
url = urlopen('http://ipv6.ncnu.org/Course/WebScraping/Slide/HTML/ex05_2_csv.html')
txt = url.read()
# print ("%s" % txt)

s = BeautifulSoup(txt, "lxml")

table = s.find_all("table", id="contentsTable")[0]
headers = table.find("thead").find_all("th")
contents = table.find("tbody").find_all("tr")
# print(table)
# print (headers)
# print (contents)

data = []
rowdata = []
for rowContent in contents:
  # print(rowContent)
  colContent = rowContent.find_all("td")
  # print(colContent)
  for content in colContent:
    contentStr = content.find("p").string
    # print(contentStr)
    rowdata.append(contentStr)
  data.append(list(rowdata))
  # empty to store others
  rowdata = []
# print (data)

# write csv file
w = csv.writer(f)
w.writerows(data)
f.close()

# store unique rows
f = open("rainfall.csv","r")
seen = set()
for line in f:
  if line in seen: continue # if duplicate then skip
  seen.add(line)
f.close()

# re-write csv file
f = open("rainfall.csv","w")
f.truncate() # clear csv file

# get title now to avoid redundant check (which would sort ugly)
title = ''
i = 1
for colTitle in headers:
  title = title + colTitle.find("p").find("a").string
  if i < len(headers):
    title = title + ','
  i = i + 1
  # print(title)
f.write(title)

# write all unique row back to original file
for line in seen:
  f.write(line)
f.close()
