# pow.py
def pow(number, exponent):
 if number == 0 and exponent == 0:
  result = "this expression is considered indeterminacy"
 else:
  result = 1
  while exponent > 0:
   result *= number
   exponent -= 1
  if exponent < 0:
   exponent = -exponent
   while exponent > 0:
    result /= number
    exponent -= 1
 return result
# HW1: refactor code pow(10,-3) -> 0.001
# r = pow(10, 3)
r = pow(10, -3)
print(r)