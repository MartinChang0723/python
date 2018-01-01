import getUserInput
import analyseUserGuess

def guess (count, answer):
  guess = getUserInput.userInput()
  status = analyseUserGuess.analyse(answer, guess)
  if status == "4A":
    return count
  else:
    print(status)
    return count + 1

