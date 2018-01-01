target = input('Please enter the file name: ')
file = open(target, 'r')
file_content = file.read()

lineCount = 0
characterCount = 0
wordCount = len(file_content.split())

for char in file_content:
  characterCount += 1
  asciiCode = ord(char)
  if asciiCode == 10:
    lineCount += 1
  
lineCount += 1
print (
  'line: ' + str(lineCount)
  + ' word: ' + str(wordCount)
  + ' character: ' + str(characterCount)
)
