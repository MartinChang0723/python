from urllib.request import urlopen
import json

response = urlopen("http://opendata2.epa.gov.tw/AQI.json").read().decode('UTF-8')
responseJson = json.loads(response)

for r in responseJson:
  if r['County'] in [u"南投縣", u"高雄市"]:
    print (r)