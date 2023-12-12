# https://github.com/dorinesinenco/EDUQATION/blob/master/programming/python/OOP/title.obj.ru.md
class Title:
 def __init__(self, text):         
  self.text = text
 def __str__(self):
  return f"-= {(self.text).upper()} =-"
t1 = Title("Programming in Python 3")
print(t1)

# https://github.com/dorinesinenco/EDUQATION/blob/master/programming/python/OOP/fruits.box.ru.md
class FruitBox:
 def __init__(self, apples, oranges):
  if type(apples) == float or type(oranges) == float:
   print("Error. Argument number cannot be float.")
   quit()
  if apples + oranges > 50:
   print("Error. Maximum box capacity is 50 fruits.")
   quit()
  self.apples = apples
  self.oranges = oranges
  
 def __add__(self, other_box):
  return FruitBox(self.apples + other_box.apples, self.oranges + other_box.oranges)
  
 def __str__(self):
        return f"The box contains {self.apples} apples and {self.oranges} oranges"

# a_box = FruitBox(10,20)

box1 = FruitBox(5, 10)  
box2 = FruitBox(10, 20)
box3 = box1 + box2
print(box1)
print(box2)
print(box3)