user_input = input('You: ')
user_input_str = str(user_input)
result = ''

for cha in user_input_str:
  if cha in ['a', 'e', 'i', 'o', 'u']:
    result += (u'\u001b[42m' + cha)
  else:
    result += (u'\u001b[0m' + cha)
print(result)