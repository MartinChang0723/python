def getCurrency():
    import socket, pickle
    (host, port) = ('STU.ipv6.club.tw', 1310)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    data = b''
    while True:
        moreData = sock.recv(4096)
        if not moreData: break
        data += moreData
    sock.close()

    aList = pickle.loads(data)
    return aList

def main():
  list = getCurrency()
  checkList = {}
  for item in list:
    data = item.split(' ')
    checkList[data[1]] = {
      'name': data[0],
      'buy': data[2],
      'sell': data[3]
    }

  while True:
    userInput = str(input("Which currency do you want to query? "))
    if userInput == '':
      break
    key = '(' + userInput.upper() + ')'
    try:
      # print(checkList[key])
      print('美金 ' + key + ' ' + checkList[key]['buy'] + '買入 ' + checkList[key]['sell'] + '賣出')
    except:
      print('No transaction on '+ userInput.upper() +' today.')




if __name__ == "__main__":
  main()
