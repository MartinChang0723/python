import printInfo
import generate4Digits
import userGuess

# 程式進入點
def main () :
  target = generate4Digits.generate4Digit()
  # printInfo.info()
  # print(target)
  count = 1
  nextCount = userGuess.guess(count, target)
  while count < nextCount:
    count = nextCount
    nextCount = userGuess.guess(count, target)
  printInfo.end(count)
if __name__ == "__main__":
  main()