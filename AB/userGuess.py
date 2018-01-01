import getUserInput
import analyseUserGuess

def guess (count, answer):
  # 讀使用者輸入
  guess = getUserInput.userInput()
  # 判斷使用者輸入的答案
  status = analyseUserGuess.analyse(answer, guess)
  if status == "4A":
    return count
  else:
    print(status)
    return count + 1

