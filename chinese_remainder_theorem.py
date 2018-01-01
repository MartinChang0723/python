r3 = int(input('N % 3 = ? '))
r5 = int(input('N % 5 = ? '))
r7 = int(input('N % 7 = ? '))

# 0~105
result = 'N = '
for i in range(105 + 1):
  if i % 3 == r3:
    if i % 5 == r5:
      if i % 7 == r7:
        result += str(i) + ' '
print (result)

# print (str((r3 * 70 + r5 * 21 + r7 * 15) % 105))