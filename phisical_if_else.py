# physical.py
class Dimension:
 allowed_units = ("m", "cm", "mm")
 def __init__(self, value, unit):
  #print(self.allowed_units)
  #print(Dimension.allowed_units)
  if unit in self.allowed_units:
   self.value = value
   self.unit = unit
  else:
   print(f"Error: {unit} is not allowed.")
 def __str__(self):
  return f"{self.value}{self.unit}"
 def __add__(self, other):
# hm1: using if/else or match/case
# make it so if 2 diff units
# switch to the minimal unit
  if self.unit != other.unit:
# variant using if/else
   if self.unit == 'mm' and other.unit == 'cm':
    other.value *= 10
    unit = self.unit
   elif self.unit == 'cm' and other.unit == 'mm':
    self.value *= 10
    unit = other.unit
   elif self.unit == 'cm' and other.unit == 'm':
    other.value *= 100
    unit = self.unit
   elif self.unit == 'm' and other.unit == 'cm':
    self.value *= 100
    unit = other.unit
   elif self.unit == 'mm' and other.unit == 'm':
    other.value *= 1000
    unit = self.unit
   elif self.unit == 'm' and other.unit == 'mm':
    self.value *= 1000
    unit = other.unit
# end of variant using if/else
  else:
   unit = self.unit
  value = self.value + other.value
  return Dimension(value, unit)
# 3d dimensions of a box
length_1 = Dimension(6, 'm')
length_2 = Dimension(4, 'm')

#            Dimension  Dimension
#                v          v
length_total = length_1 + length_2 # -> int
#                v          v
#  __add__     (self,      other)
print(length_total)
print(type(length_total))

length_1 = Dimension(7, 'mm')
length_2 = Dimension(3, 'cm')
length_total = length_1 + length_2
print(length_total)
length_1 = Dimension(7, 'cm')
length_2 = Dimension(3, 'mm')
length_total = length_1 + length_2
print(length_total)
length_1 = Dimension(7, 'cm')
length_2 = Dimension(3, 'm')
length_total = length_1 + length_2
print(length_total)
length_1 = Dimension(7, 'm')
length_2 = Dimension(3, 'cm')
length_total = length_1 + length_2
print(length_total)
length_1 = Dimension(7, 'mm')
length_2 = Dimension(3, 'm')
length_total = length_1 + length_2
print(length_total)
length_1 = Dimension(7, 'm')
length_2 = Dimension(3, 'mm')
length_total = length_1 + length_2
print(length_total)