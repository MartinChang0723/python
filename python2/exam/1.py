import os
import csv

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
  result = []
  existedYear = []
  fileName = os.listdir('./')
  for name in sorted(fileName):
    if '.csv' in name:
      f = open(name)
      stock = csv.reader(f)
      i = 0
      for line in stock:
        if i == 2:
          try:
            year = line[0].split('/')[0]
            if (year not in existedYear):
              existedYear.append(year)
              price = line[6]
              result.append((year, price))
              # print(year + ' ' + price)
              break
            else:
              pass
          except:
            print (i)
        i = i + 1
      f.close()

  for d in sorted(result, key=lambda r: r[0]):
    print(d[0], d[1])

if __name__ == "__main__":
  main()
