# 2d-matrix-func.py
# * * *
# * * *
# * * *
def printStar():
 print('*', end = " ")

def printStarRow(w):
 for i in range(w):
  printStar()
 print()
  
def printstarRect(w, h):
 if w > 0 and h > 0:
  for i in range(h):
   printStarRow(w)
 else:
  print("Cannot use NEGATIVE dimensions!")

printstarRect(5, 3)

# hm1: draw complete diagram
# printstarRect(w, h):
#  |
#  v
# call->printstarRect(w = 5, h = 3)
#        |
#        v
#     if w > 0 and h > 0 ->False->else
#        v                         v
#       True           print("Cannot use ...")
#        v
#    ->i:0,1,2-----------------------|
#    ^   |                           |
#    |   v->call printStarRow(w = 3) |
#    |            |                  |
#    |            v                  |
#    |        ->i:0,1,2,3,4---------||
#    |        ^   |                 ||
#    |        |   v->call print("*")||
#    |        |<-----------         ||
#    |<--------------call print()<--||
#               v--------------------|
#   <-----------v
#   |
#   v