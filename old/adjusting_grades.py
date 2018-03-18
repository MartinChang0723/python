from math import sqrt
userInput = input('Input the original grade -- ')
grade = int(userInput)

adjusted_grade = int(sqrt(grade) * 10)

output = 'The adjusted grade is ' + str(adjusted_grade) + '.'
print (output)