# app-s-ns.py
# static, non-static
class Water:
 def __init__(self, volume = 1, temp = 18):
  self.volume = volume
  self.temp = temp
  if temp > 100:
   self.state = "vapor"
  elif temp <= 0:
   self.state = "solid"
  else:
   self.state = "liquid"
 def __str__(self): 
  return f"WATER <{self.volume}L | {self.state:>7} | {self.temp}C>"
def heat(water, deltaTemp = 0):
 result = Water(water.volume, water.temp + deltaTemp)
 return result
# hm2: finish cool()
def cool(water, deltaTemp = 0):
 result = Water(water.volume, water.temp - deltaTemp)
 return result
w = Water()
print (w)
w = heat(w, 100)
print (w)
w = cool(w, 120)
print (w)