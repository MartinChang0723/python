from math import floor
user_input = input('Input the file name of grades -- ')

# create score list
scoreList = {}
for i in range(11):
  if i == 0:
    scoreList[str(i)] = 0
  else:
    scoreList[str(i) + "0"] = 0
# print(scoreList)
output = ""
with open("./" + str(user_input), "r", encoding="UTF-8") as fp:
  for line in iter(fp.readline, ''):
    n = int(line)
    floorN = str(floor(n / 10) * 10)
    scoreList[floorN] += 1
  # print(scoreList)

  for key, val in scoreList.items():
    output += key + "\t" + str(val)
    for i in range(val):
      output += "＃"
    output += "\n"
  print(output)