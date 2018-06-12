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
  downloadTSMC()
  result = {}
  existedYear = []
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
              year = line[0].split('/')[0]
              price = line[6]
              result[year] = price
            else:
              break
          except:
            pass
        i = i + 1
      f.close()

  # print(result)
  for d in sorted(result, key=lambda r: r):
    print(d + ' ' + result[d])

  import matplotlib.pyplot as plt
  plt.bar(range(len(result)), list(result.values()), align='center')
  plt.xticks(range(len(result)), list(result.keys()))
  plt.show()

if __name__ == "__main__":
  main()
