file = open('poem.txt', 'r')
file_content = file.read()
result = ''
i = 0
lengthCounter = 0 # 76 / 2 = 38
while i < len(file_content):
  if file_content[i] not in ['\n', ' ']:
    result += file_content[i]
    lengthCounter += 1
  if lengthCounter == (76 / 2):
    result += '\n'
    lengthCounter = 0
  i += 1
print (result)