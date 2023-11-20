# 2d.list.py
# bidimensional list (3 x 3) / matrix
matrix = [
 [1, 2, 3], # 0
 [4, 5, 6], # 1
 [7, 8, 9]  # 2
# 0, 1, 2
]
for ri in range(3):
 for ci in range(3):
  print(matrix[ri][ci], end = " ")
 print()
# транспонирование матрицы
for ri in range(3):
 for ci in range(3):
  print(matrix[ci][ri], end = " ")
 print()