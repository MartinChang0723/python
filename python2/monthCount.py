monthNameList = ["None Zero", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
result = {
  "Jan": 0,
  "Feb": 0,
  "Mar": 0,
  "Apr": 0,
  "May": 0,
  "Jun": 0,
  "Jul": 0,
  "Aug": 0,
  "Sep": 0,
  "Oct": 0,
  "Nov": 0,
  "Dec": 0
}
output = ""
with open("./2014_news.txt", "r", encoding="UTF-8") as fp:
  for line in iter(fp.readline, ''):
    splitLine = line.split("＊")
    # splitLine: __0__ * __1__
    date = splitLine[0]
    report = splitLine[1]
    # date: __0__ / __1__ / __2__
    month = int(date.split("/")[1])
    result[monthNameList[month]] += 1
  # print(result)
for key, val in result.items():
  # print(key, val)
  output += key + "\t" + str(val) + "\t"
  for i in range(val):
    output += "*"
  output += "\n"
print(output)