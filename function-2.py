# function-2.py
# - generate random 2d array
# - print 2d array
# - calculate the average value of 2d array
# srp - simple responsibility principle, принцип единственной ответственности, обозначающий, что каждая функция должна иметь одну ответственность. Все поведения функции должны быть направлены исключительно на обеспечение этой ответственности.

from random import randint
# hm1: pass value range as arguments
def random2dArray(rows, cols, min, max):
 matrix = []
 for ri in range(rows):
  row = []
  for ci in range(cols):
   row. append (randint(min, max))
  matrix .append(row)
 return matrix

# hm2: add a header
# size 5 x 3
def print2dArray(matrix):
 print()
 print("size ", len(matrix), " x ",len(matrix[0]))
 for ri in range(len(matrix)):
  for ci in range(len(matrix[0])):
   print(f" {matrix[ri][ci]:5} ", end="")
  print()
 
# hm3: create another function that finds min, max values, returns grouped
def minmax2dArray(matrix):
 min = max = matrix[0][0]
 for ri in range(len(matrix)):
  for ci in range(len(matrix[0])):
   if matrix[ri][ci] < min:
    min = matrix[ri][ci]
   if matrix[ri][ci] > max:
    max = matrix[ri][ci]
 return [min, max]

def average2dArray(matrix):
 s = 0
 w = len(matrix[0])
 h = len(matrix)
 for ri in range(h):
  for ci in range(w):
   s += matrix[ri][ci]
 average = s / (h * w)
 return average
data = random2dArray(5 ,3, 0, 10)
print2dArray(data)
print(minmax2dArray(data))
a = average2dArray(data)
print(a)
