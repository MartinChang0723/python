targets = ["自信", "有信心", "樂觀", "看好", "成長", "積極", "買進", "增加持股" "賣出"]
result = ""
with open("./s104214001.txt", "r", encoding="UTF-8") as fp:
  for line in iter(fp.readline, ''):
    cache_str = ""
    for t in targets:
      cache_str = line.replace(t, u'\u001b[32m' + t + u'\u001b[0m')
      result += cache_str
print(result)