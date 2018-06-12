from urllib.request import urlopen
import json
import ssl 
context = ssl._create_unverified_context() 

response = urlopen("https://api.ncnu.edu.tw/API/get.aspx?json=info_ncnu&month_include=6", context=context).read().decode('UTF-8')
responseJson = json.loads(response)

result = []

for r in responseJson['info_ncnu']['item']:
  result.append((int(r['count']), r['title'], r['created_at']))

for i in sorted(result, key=lambda r: r[0], reverse=True):
  print (str(i[0]) + ' ' + i[2] + ' ' + i[1])