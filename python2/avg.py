import csv

def toPrecision2(n):
  return "%0.2f" % (n)

def avgNumberArray(arr, days):
  sumN = 0
  for i in arr:
    sumN = i + sumN
  return toPrecision2(sumN / days)

fname = './ch06_tsmc.csv'
f = open(fname,"r")
index = 0
sumPrice = 0
finalResult = [
  ['Date', 'closingPrice', 'avg5', 'avg20', 'avg60'] # header
]
arr5 = []
arr20 = []
arr60 = []

for line in f:
  if index > 0:
    strList = line.split(',')
    date = strList[0]
    closingPrice = float(strList[4])
    sumPrice = sumPrice + closingPrice

    dailyResult = [date, str(closingPrice), '', '', '']

    arr5.append(closingPrice)
    arr20.append(closingPrice)
    arr60.append(closingPrice)
    if len(arr5) == 5:
      dailyResult[2] = avgNumberArray(arr5, 5)
      # remove head
      arr5.pop(0)
    if len(arr20) == 20:
      dailyResult[3] = avgNumberArray(arr20, 20)
      # remove head
      arr20.pop(0)
    if len(arr60) == 60:
      dailyResult[4] = avgNumberArray(arr60, 60)
      # remove head
      arr60.pop(0)
    
    finalResult.append(dailyResult)

  index = index + 1

# re-write csv file
f = open(fname,"w")
f.truncate() # clear csv file
w = csv.writer(f) # write csv file
w.writerows(finalResult)
f.close()
