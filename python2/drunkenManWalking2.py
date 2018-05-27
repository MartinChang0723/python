from random import randint
def toPrecision2(n):
  return "%0.2f" % (n)
def simOneIteration (n) :
  while (10 > n > 0):
    direction = randint(0, 1)
    if direction == 0:
      n = n + 1
    else:
      n = n - 1
  if n == 10:
    return True
  elif n == 0:
    return False

while True:
  inStr = input("Input the initial position and number of iterations (p, n) -- ")
  inArr = inStr.replace(' ', '').split(',')
  if len(inArr) < 2:
    print("Invalid input")
    # continue
  else:
    p = int(inArr[0])
    n = int(inArr[1])
    home = 0
    river = 0
    while n > 0:
      temp = simOneIteration(p)
      # print (temp)
      if temp:
        home = home + 1
      else:
        river = river + 1
      n = n - 1
    print("Probability:")
    print("Home\t", str(home), '\t', toPrecision2(home / (home + river) * 100) + '%')
    print("River\t", str(river), '\t', toPrecision2(river / (home + river) * 100) + '%')
