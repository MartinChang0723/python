import time
from random import randint


p = ''
pN = 0
n=""
nn=0
while True:
  p = input("Input the initial position  (p)")
  pN = int(p)
  if pN >= 10:
    print('input too big, only 1~9 is valid.')
  elif pN <= 0:
    print('input too small, only 1~9 is valid.')
  else:
    break

n=input("number of iteration")
nn=int(n)


def printArr (arr) :
  myStr = ''
  for i in arr:
    myStr = myStr + str(i)
  print (myStr)

def simOneIteration (c) :
  road = ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|']
  road[c] = '*'
  printArr(road) 

  

    
while (10 > pN > 0):
  simOneIteration(pN)
  direction = randint(0, 1)
  if direction == 0:
    pN = pN + 1
  else:
    pN = pN - 1

for i in range(1,n):
    
   
#if (pN == 10):
  #print ('He falls into a river in a cold winter!')
#elif (pN == 0):
  #print ('He arrives home safely.')


