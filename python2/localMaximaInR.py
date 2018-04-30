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
  return result

def main ():
  r = 2
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
    if isLocalMaximaInR(priceList, i, r):
      result = dateList[i] + '\t'
      for j in range(1, r + 1):
        result += (str(priceList[i-j]) + '\t')
      result += str(priceList[i]) + '\t'
      for j in range(1, r + 1):
        result += (str(priceList[i+j]) + '\t')
      print(result)

if __name__ == "__main__":
  main()