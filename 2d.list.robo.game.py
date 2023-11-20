# 2d.list.robo.game.py
from os import system
from random import randint
# game map - list 10 x 10
# - why ints ?
# legend:
# 0 - empty
# 1 - robot
rx = randint(0, 9)
ry = randint(0, 9)
# 2 - bomb
bx = 3
by = 3
if ry == by and rx == 9 and bx == 9:
 rx -= 1;
elif ry == by and rx == bx:
 rx += 1;
game_over = False
gm = [
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # trailing comma - dont warry
]
gm[ry][rx] = 1 # initial robot coord setup
gm[by][bx] = 2 # initial bomb coord setup
while True:
# draw the map
 system("clear")
 print("#" * 20)
 for y in range(10):
  for x in range(10):
  # print(gm[y][x], end = " ")
   if gm[y][x] == 1:
    print("R", end = " ")
   elif gm[y][x] == 2:
    print("X", end = " ")
   elif gm[y][x] == 3:
    print("B", end = " ")
    game_over = True
   else:
    print(".", end = " ")
  print()
 print("#" * 20)
 if game_over:
  break
 option = input(">>> ")
# hm2: optimize movement ?
# hm3*: check the bomb / hp
 if option == "d" and rx < 9:
  gm[ry][rx] = 0 # delete the robot
  rx += 1
  gm[ry][rx] = 1 # put the robot back
 elif option == "a" and rx > 0:
  gm[ry][rx] = 0
  rx -= 1
  gm[ry][rx] = 1
 elif option == "s" and ry < 9:
  gm[ry][rx] = 0
  ry += 1
  gm[ry][rx] = 1
 elif option == "w" and ry > 0:
  gm[ry][rx] = 0
  ry -= 1
  gm[ry][rx] = 1
 if ry == by and rx == bx:
  gm[ry][rx] = 3 
# hm1: add move left / up
