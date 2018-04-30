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
  for line in f:
    strList = line.split('\",\"')
    priceList.append(strList[6])
  f.close()
  # print(priceList)
  maximaList = []
  for i in range(1, len(priceList) - 1):
    if isLocalMaxima(priceList, i):
      maximaList.append(priceList[i])
  print(maximaList)
  
if __name__ == "__main__":
  main()