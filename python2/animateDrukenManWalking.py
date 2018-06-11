from random import randint
from time import sleep
p = ''
pN = 0
while True:
  p = input("Input the initial position (p) -- ")
  pN = int(p)
  if pN >= 10:
    print('input too big, only 1~9 is valid.')
  elif pN <= 0:
    print('input too small, only 1~9 is valid.')
  else:
    break

def printArr (arr) :
  myStr = ''
  for i in arr:
    myStr = myStr + str(i)
  print (myStr, end="\r")

def simOneIteration (n) :
  road = ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|']
  road[n] = '*'
  printArr(road)
  sleep(1)
    
while (10 > pN > 0):
  simOneIteration(pN)
  direction = randint(0, 1)
  if direction == 0:
    pN = pN + 1
  else:
    pN = pN - 1

if (pN == 10):
  print ('He falls into a river in a cold winter!')
elif (pN == 0):
  print ('He arrives home safely.')
