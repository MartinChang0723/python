import os
import csv
import pandas

def downloadTSMC():
    from urllib.request import urlretrieve
    urlBase = "http://ipv6.ncnu.org/Course/FinTech/Exercise/Final/"
    for y in range(2000, 2019):
        for m in range(1, 13):
            if y == 2018 and m == 7: break
            fn = "tsmc-{}{:02}.csv".format(y, m)
            urlretrieve(urlBase+fn, fn)

def main () :
  # downloadTSMC()
  result = []
  fileName = os.listdir('./')
  for name in sorted(fileName):
    if '.csv' in name:
      f = open(name)
      stock = csv.reader(f)
      i = 0
      prevLine = []
      for line in stock:
        if i > 1:
          try:
            if '說明:' not in line:
              result.append([str(line[0]), str(line[1]).replace(',', ''), str(line[2]).replace(',', ''), str(line[3]), str(line[4]), str(line[5]), str(line[6]), str(line[7]), str(line[8]).replace(',', '')])
            else:
              break
          except:
            pass
        i = i + 1
      f.close()

  f = open('total.csv',"w")
  f.truncate() # clear csv file
  w = csv.writer(f) # write csv file
  w.writerows(result)
  f.close()

if __name__ == "__main__":
  main()
