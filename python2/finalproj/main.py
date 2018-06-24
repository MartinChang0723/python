# https://github.com/pyexcel/pyexcel-xlsx
from pyexcel_xlsx import get_data, save_data
from collections import OrderedDict

# http://pydash.readthedocs.io/en/latest/api.html#module-pydash.strings
import pydash

import statistics
import json

inputFileName = "PRICE PYTHON.xlsx"

### save data to json (will be faster to read and write)
print("讀取原始資料...", end=" ")
data = get_data(inputFileName)
print("建立JSON...", end="")
with open("data.json", "w") as outfile:
  json.dump(data, outfile)
print("已完成")

### read data from json to analyze
print("讀取JSON...", end="")
with open("data.json", encoding='utf-8-sig') as json_file:
  json_data = json.load(json_file)
  fundData = json_data["PRICE PYTHON"]
print("已完成")

### get all type of 基金 and transform fundData into groups of each type
print("資料整理...", end="")
groupedFundData = {}
for index, record in enumerate(fundData):
  if index > 0:
    # fundName = record[1].strip()
    fundCode = record[0]
    fundName = record[1]
    fundISIN = record[2]
    fundTime = record[3]
    fundPrice = record[4]
    fundRange = record[5]
    # handle record error situation like [649, 'FH香港', 'TW0000064906', 20160113, 15, '          .']
    if type(fundRange) is str:
      # print(record)
      fundRange = 0

    try:
      groupedFundData[fundName]
    except:
      groupedFundData[fundName] = []
      pass
    groupedFundData[fundName].append([
      fundCode,
      fundName,
      fundISIN,
      fundTime,
      fundPrice,
      fundRange
    ])
# print(groupedFundData)
print("已完成！")

### caculate
print("資料分析...", end="")
analyzedData = {}
for name, data in groupedFundData.items():
  # print(name)

  # unzip data (http://pydash.readthedocs.io/en/latest/api.html#pydash.arrays.unzip)
  colunmlizedData = pydash.unzip(data)
  # 淨值變動率
  analyzedData[name] = {}
  analyzedData[name]["Name"] = name
  analyzedData[name]["平均報酬"] = statistics.mean(colunmlizedData[5])
  if len(colunmlizedData[5]) < 2:
    analyzedData[name]["標準差"] = 1
  else:  
    analyzedData[name]["標準差"] = statistics.stdev(colunmlizedData[5])
  if analyzedData[name]["標準差"] == 0:
    analyzedData[name]["SharpeIndex"] = 0
  else:
    analyzedData[name]["SharpeIndex"] = (analyzedData[name]["平均報酬"] - 0.79) / analyzedData[name]["標準差"]
analyzedData = pydash.order_by(analyzedData, ["平均報酬"], [False])
# print(analyzedData)
print("已完成！")

### export to excel
print ("資料匯出...", end="")
exportData = [["Name", "平均報酬", "標準差", "SharpeIndex"]]
chartData = {"names": [], "value": []}
iii = 0
for data in analyzedData:
  exportData.append([
    data["Name"].strip(),
    data["平均報酬"],
    data["標準差"],
    data["SharpeIndex"]
  ])
  if iii < 10:
    chartData["names"].append(data["Name"].strip())
    chartData["value"].append(data["平均報酬"])
  iii = iii + 1
# print(exportData)
data = OrderedDict() # from collections import OrderedDict
data.update({"FundReport": exportData})
save_data("FundReport.xlsx", data)
print("已完成！")

# import pandas
# data = pandas.Series(chartData["value"], index=chartData["names"])
# data.plot()
# import matplotlib.pyplot as plt
# plt.show()

import matplotlib.pyplot as plt
plt.bar(range(len(chartData["value"])), chartData["value"], align='center')
plt.xticks(range(len(chartData["names"])), chartData["names"])
plt.show()