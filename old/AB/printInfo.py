
import time
def info () :
  print("Wanna play a game?")
  time.sleep(1)
  print("There's a four digit number for you to guess.")
  time.sleep(2)
  print("I'll give you an 4A if your answer is correct.")
  time.sleep(2)
  print("And if you have one integer's position is wrong, you'll get 3A1B... something like that.")
  time.sleep(3)
  print("If you can get it right in 10 guess, I'll let you live...")
  time.sleep(3)
  print("If more, you better watchout! Hehehe.............")
  time.sleep(3)

def end (count) :
  print("Correct! You've tried: " + str(count) + " times.")
  if count > 10:
    time.sleep(2)
    print("But you've guessed too many times...")
    time.sleep(1)
    print("See ya 🔪 🔪 🔪 🔪 🔪 🔪 🔪 🔪 🔪 🔪 🔪 🔪 🔪 🔪 🔪 🔪 🔪 🔪 🔪 🔪 🔪 🔪 🔪")