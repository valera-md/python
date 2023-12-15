# app_water.py
# class - Abstraction / instance (object)
class Water:
# functional: default arg value
# oop: polymorphism / overload
 def __init__(self, volume = 0):
  if self.isNumber(volume):
   self.volume = volume
  elif type(volume) == str and volume in ["large", "medium", "small"]:
   if volume == "large":
    self.volume = 1000
   elif volume == "medium":
    self.volume = 100
   elif volume == "small":
    self.volume = 10
  else:
   print("Error. Wrong volume value.")
 def __str__(self):
  return f"WATER <{self.volume}L>"
 def __len__(self):
  return self.volume
# overloading
#          obj1.method
#          obj1 > obj2
#            v     v
 def __gt__(self, other):
  if self.isNumber(other):
   return self.volume > other
  else:
   return self.volume > other.volume
# hm1: operatirs: < >= <= == !=
 def __lt__(self, other):
  if self.isNumber(other):
   return self.volume < other
  else:
   return self.volume < other.volume
 def __ge__(self, other):
  if self.isNumber(other):
   return self.volume >= other
  else:
   return self.volume >= other.volume
 def __le__(self, other):
  if self.isNumber(other):
   return self.volume <= other
  else:
   return self.volume <= other.volume
 def __eq__(self, other):
  if self.isNumber(other):
   return self.volume == other
  else:
   return self.volume == other.volume
 def __ne__(self, other):
  if self.isNumber(other):
   return self.volume != other
  else:
   return self.volume != other.volume
#           obj1 + obj2
 def __add__(self, other):
  return Water(self.volume + other.volume)
 def isNumber(self, value):
  return type(value) == int or type(value) == float
# REAL WORLD: Water ? Abstraction vs Concrete
largeWater = Water(1000)
smallWater = Water(10)
emptyWater = Water()
mediumWater = Water("medium")
print(largeWater > smallWater)
print(largeWater > 900)
print(smallWater < mediumWater)
print(smallWater < 900)
print(largeWater >= mediumWater)
print(largeWater >= 900)
print(largeWater >= largeWater)
print(largeWater >= 1000)
print(smallWater <= largeWater)
print(smallWater <= 900)
print(smallWater <= smallWater)
print(smallWater <= 10)
print(largeWater == largeWater)
print(mediumWater == 100)
print(largeWater != smallWater)
print(mediumWater != 1000)
#print(len(largeWater))
#print(len(smallWater))
#print(len(emptyWater))
print(largeWater)
print(smallWater)
print(emptyWater)
print(mediumWater)
resultWater = largeWater + mediumWater # 1000 + 100 -> 1100
print(resultWater)