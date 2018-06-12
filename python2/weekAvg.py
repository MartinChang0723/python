import csv
import pandas
from datetime import datetime

def dow(dstr):
  dateArr = dstr.split('/')
  return datetime(int(dateArr[0]), int(dateArr[1]), int(dateArr[2])).weekday()

def toPrecision2(n):
  return "%0.2f" % (n)

def avgNumberArray(arr, days):
  sumN = 0
  for i in arr:
    sumN = i + sumN
  return toPrecision2(sumN / days)

fname = './ch06_tsmc.csv'
f = open(fname,"r")
sumReturns = [0.0, 0.0, 0.0, 0.0, 0.0]
cntReturns = [0, 0, 0, 0, 0]
result = []
index = 0
for line in f:
  if index > 0:
    strList = line.split(',')
    wkday = dow(strList[0])
    re = float(strList[5])
    if wkday > 4:
      wkday = wkday % 5
    sumReturns[wkday] = re
    cntReturns[wkday] = cntReturns[wkday] + 1
  index = index + 1

for index, su in enumerate(sumReturns):
  result.append(su / cntReturns[index])

print(result)
data = pandas.Series(result, index=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
data.plot()
import matplotlib.pyplot as plt
plt.show()