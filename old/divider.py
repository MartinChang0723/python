userInput = input('Input: ')
inputNum = int(userInput)
divider = 2
result = ''

if inputNum < 2:
  print (inputNum)
else:
  while divider <= inputNum:
    while inputNum % divider == 0:
      inputNum /= divider
      result = result + str(divider) + ' * '
    divider += 1
  print (result[:-3])
 