# human-objects.py
class Human:
 def __init__(self, name, year_of_birth):
  self.name = name
  self.year_of_birth = year_of_birth
 def eat(self, what):
# hm1: modify code of this method
# MnomMnom ... Adam eating {what}
  print(f"MnomMnom ... {self.name} eating {what}")
 def printAge(self):
  print(2022 - self.year_of_birth)
 def __gt__(self, other):
  return self.year_of_birth < other.year_of_birth
# use the class as factory
h1 = Human("Adam", -6000)
h1.money = 10000
h2 = Human("John", 2000)
print(h1 > h2)
print(h1.name)
h1.printAge()
print(h1.money)
print(h2.name)
h2.printAge()
h1.eat("salad")
h2.eat("borsch")