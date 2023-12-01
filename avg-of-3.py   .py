+----- main program ------------------------+
| a = 10                                    |
| b = 20                                    |
| c = 30                                    |
|         a     b     c                     |
| call    |     |     |                     |
|    \    v     v     v                     |
| +-avg(par1, par2, par3)--+                |
| | s = par1 + par2 + par3 |                |
| | m = s / 3              |                |
| +- return m -------------+                |
|           |                               |
|           v                               |
|          res                              |
|                                           |
|                   a     b     c   res     |
| call              |     |     |    |      |
|    \              v     v     v    v      |
| +-printFormated(par1, par2, par3, res)--+ |    | | print(f"the average of                | |
| | {par1} {par2} {par3} is {res}")       | |
| +---------------------------------------+ |
|                                           |
+-------------------------------------------+

# avg-of-3.py
def avg(par1, par2, par3):
 s = par1 + par2 + par3
 m = s / 3
 return m
def printFormated(par1, par2, par3, res):
 print(f"the average of {par1} {par2} {par3} is {res}")
# MAIN PROGRAM
a = 10
b = 20
c = 30
# function frame
# > call
res = avg(a,b,c)
# < return
# /function frame
# print(f"the average of {a} {b} {c} is {res}")
printFormated(a, b, c, res)
# /MAIN PROGRAM
