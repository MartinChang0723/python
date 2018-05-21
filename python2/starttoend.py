import csv
from datetime import datetime

def dow(dstr):
  dateArr = dstr.split('/')
  if int(dateArr[0]) < 1900:
    year = 1911 + int(dateArr[0])
  else: year = int(dateArr[0])
  return datetime((year), int(dateArr[1]), int(dateArr[2])).weekday()

nStart = { 'i': -1, 'day': '' }
nEnd = { 'i': -1, 'day': '' }
weekStrArr = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# fname = './ch07_cht.csv'
fname = './ch07_tsmc.csv'
f = open(fname)
stock = csv.reader(f)
for line in stock:
  date = line[0]
  dayN = dow(line[0])
  day = weekStrArr[dayN]
  if nStart['i'] == -1:
    nStart = {
      'i': dayN,
      'day': date
    }
    nEnd['i'] = dayN
  else:
    if dayN > nEnd['i']:
      nEnd = {
        'i': dayN,
        'day': date
      }
    elif dayN < nEnd['i']:
      print (nStart['day'] + ' ' + weekStrArr[nStart['i']] + ' ' + nEnd['day'] + ' ' + weekStrArr[nEnd['i']])
      nStart = {
        'i': dayN,
        'day': date
      }
      nEnd = {
        'i': dayN,
        'day': date
      }