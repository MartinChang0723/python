import csv

def isLocalMaximaInR(aList, index, r=1):
  result = True
  target = float(aList[index])
  for i in range(1, r + 1):
    try:
      before = float(aList[index - i])
      if target < before:
        result = False
        break
      after = float(aList[index + i])
      if target < after:
        result = False
        break
    except:
      pass
  print (result)
  return result

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