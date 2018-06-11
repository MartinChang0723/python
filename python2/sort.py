import csv
fname = './stock_date.csv'
f = open(fname,"r")
tutu = []
for line in f:
  print(line)
  strList = line.split(',')
  code = strList[0]
  date = strList[1]
  tutu.append((code + date, line))

print(sorted(tutu, key=lambda tu: tu[0]))