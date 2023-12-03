# recursion.py
def increaseInt(n):
 n += 1
 return n
# hm3: draw the memory diagram
n = 1
n = increaseInt(n)
print(n)

              args
   call        |
      \        v
+---- __main__() ------+
| n = 1                |
|                n     |
|  call          |     |
|    \           v     |
| +- increaseInt(n) -+ |
| | n += 1           | |
| +---- return n ----+ |
|              |       |
|         n = <-       |      
+--- return -----------+

# hw4: try to modify the code so it prints 7 6 5 4 3 2 1

def decreaseInt(n):
 print(n)
 n -= 1
 if n != 0:
  return decreaseInt(n)
 else:
  return
n = 7
decreaseInt(n)