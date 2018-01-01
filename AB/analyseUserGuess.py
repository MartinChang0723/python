def analyse (answer, guess) :
  result = ""
  A = 0
  B = 0
  if guess == 'help':
    return answer
  else:
    # "apple" => list: ["a", "p", "p", "l", "e"]
    answer = list(answer)
    guess = list(guess)
    # enumerate() => index, char
    # if no enumerate() => 就沒有 index
    for index, char in enumerate(guess): # A
      # index: 0,
      # char: "a"
      # answer: 1234
      # guess: 0199
      try:
        position = answer.index(char)
        if position == index:
          A += 1
          answer[index] = 'x'
      except:
        pass
    for index, char in enumerate(guess): # B
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
  