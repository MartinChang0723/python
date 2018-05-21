import csv
from datetime import datetime

def dow(dstr):
  dateArr = dstr.split('/')
  if int(dateArr[0]) < 1900:
    year = 1911 + int(dateArr[0])
  else: year = int(dateArr[0])
  return weekStrArr[datetime((year), int(dateArr[1]), int(dateArr[2])).weekday()]

weekStrArr = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# fname = './ch07_cht.csv'
fname = './ch07_tsmc.csv'
f = open(fname)
stock = csv.reader(f)
for line in stock:
  print(line[0], dow(line[0]), line[7])