strArr = []
countArr = {}
with open('stockName.txt') as fil:
  for fl in fil:
    line = fl.strip()
    if line not in strArr:
      strArr.append(line)
      countArr[line] = 1
    else:
      countArr[line] = countArr[line] + 1

for i in strArr:
  print (i + ' ' + str(countArr[i]))