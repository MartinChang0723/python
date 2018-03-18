user_input = input('N=? ')
# print (user_input)
N = int(user_input)

sum = 0
for i in range(2 * N - 1):
  j = i + 1
  if j % 2 == 1:
    if j < 10:
      # print (j)
      sum += j
print (sum)