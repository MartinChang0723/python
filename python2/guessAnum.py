from random import randint

def userInput () :
  guess = input("x=? ")
  return int(guess)

def main () :
  ans = randint(1, 100)
  # print(ans)
  count = 0
  while True:
    ui = userInput()
    count = count + 1
    if ui > ans:
      print('Too large')
    elif ui < ans:
      print('Too small')
    else:
      print('Yes.  The number is ' + str(ans) + ' .')
      print('You successfully guess the number at the ' + str(count) + ' th time. ')
      break
  
if __name__ == "__main__":
  main()