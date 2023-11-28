# hm_function.py
# https://github.com/dorinesinenco/EDUQATION/blob/master/programming/python/functional/wrappers.ru.md
def wrap_brackets(text):
 return "(" + text + ")"
# print(wrap_brackets("12345"))
def wrap_square_brackets(text):
 return "[" + text + "]"
def wrap_angle_brackets(text):
 return "<" + text + ">"
s = "12345"
s = wrap_brackets(s)
s = wrap_square_brackets(s)
s = wrap_square_brackets(s)
s = wrap_square_brackets(s)
s = wrap_angle_brackets(s)
s = wrap_angle_brackets(s)
s = wrap_angle_brackets(s)

# https://github.com/dorinesinenco/EDUQATION/blob/master/programming/python/functional/input.helpers.ru.md
def inputInt(message):
 return int(input(message))
n = inputInt("Enter the first integer: ")
m = inputInt("Enter the second integer: ")
print(n + m)
def inputFloat(message):
 return float(input(message))
n = inputFloat("Enter the first float number: ")
m = inputFloat("Enter the second float number: ")
print(n + m)
def inputBoolean(message):
 return bool(input(message))
n = inputBoolean("Enter a value to convert it to boolean type and check the truth or falsity of this value: ")
print(n)

# https://github.com/dorinesinenco/EDUQATION/blob/master/programming/python/functional/draw.lines.ru.md
def drawLine(length, direction):
 if(direction == 'h'):
  print("-" * length)
 elif(direction == 'v'):
  print("|\n" * length)
drawLine(5, 'h')
drawLine(3, 'v')