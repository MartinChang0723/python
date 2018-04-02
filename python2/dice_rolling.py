import random
count = [ 0 ] * 11
result = {}
for i in range(13):
  if i > 1:
    result[str(i)] = 0
for i in range(100):
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  i = dice1 + dice2
  result[str(i)] += 1
  # print( dice1, '+', dice2, '=', i)
# print(result)

for key, val in result.items():
  print(key + ' - ' + str(val))
