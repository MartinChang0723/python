import random

def generate4Digit () :
  ran = random.randint(0,9999)
  if ran < 1000:
    # 個位數
    if ran < 10:
      return "000" + str(ran)
    # 剩下兩位數、三位數的判斷.........

# print(generate4Digit())