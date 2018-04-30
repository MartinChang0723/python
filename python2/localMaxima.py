import csv

def isLocalMaxima(aList, index):
  target = float(aList[index])
  before = float(aList[index - 1])
  after = float(aList[index + 1])
  if target > before:
    if target > after:
      return True
    else:
      return False
  else:
    return False 


def main ():
  f = open("tsms.csv","r")
  priceList = []
  dateList = []
  for line in f:
    strList = line.split('\",\"')
    dateList.append(strList[0].replace('\"', ''))
    priceList.append(strList[6].replace('\"', ''))
  f.close()
  # print(priceList)
  maximaList = []
  for i in range(1, len(priceList) - 1):
    if isLocalMaxima(priceList, i):
      print(dateList[i] + '\t' + str(priceList[i-1]) + '\t' +  str(priceList[i]) + '\t' +  str(priceList[i+1]) )
  
if __name__ == "__main__":
  main()