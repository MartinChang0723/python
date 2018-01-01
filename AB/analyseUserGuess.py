def analyse (answer, guess) :
  result = ''
  A = 0
  B = 0
  if guess == 'help':
    return answer
  else:
    answer = list(answer)
    guess = list(guess)
    for index, char in enumerate(guess):
      try:
        position = answer.index(char)
        if position == index:
          A += 1
          answer[index] = 'x'
      except:
        pass
    for index, char in enumerate(guess):
      try:
        position = answer.index(char)
        if position != index:
          B += 1
      except:
        pass
      # print(guess, answer)
    if A > 0:
      result += str(A) + 'A'
    if B > 0:
      result += str(B) + 'B'
    return result
  