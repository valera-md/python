# https://github.com/dorinesinenco/EDUQATION/blob/master/programming/python/OOP/container.tuple.ru.md
class Container:
 def __init__(self, first = None,second = None):
  if first == None or second == None:
   self.first = first
   self.second = second
  elif first < second:
   self.first = first
   self.second = second
  else:
   self.first = second
   self.second = first
  
 def __str__(self):
  return f"[{self.first}, {self.second}]"
  
 def __eq__(self, other):
  return self.first == other.first and self.second == self.second
    
c1 = Container()
c2 = Container(10)
c3 = Container(10, 100)
c4 = Container(100, 10)
c5 = Container(10, 100)

print(c1)
print(c2)
print(c3)
print(c4)
print(c3 == c5)

# https://github.com/dorinesinenco/EDUQATION/blob/master/programming/python/OOP/product.obj.class.p1.ru.md

Какую роль играет init() ?
Метод __init__ в Python играет роль конструктора.
__init __() – это встроенная функция в Python, которая вызывается всякий раз, когда создается объект. __init __() инициализирует начальное состояние объекта. Функции __init__() мы можем передавать аргументы, через которые инициализируем некоторые атрибуты (свойства) объекта.

Почему метод init - принимает аргумент self и откуда он берется?
Метод __init__ принимает self в качестве первого параметра, остальные параметры это значения, которые передаются при создании нового объекта класса, и они устанавливаются в качестве атрибутов объекта.
self — это ссылка на текущий экземпляр класса. Это способ обращения к атрибутам и методам класса изнутри самого класса.
self не передается при создании нового объекта класса. Python автоматически передает ссылку на текущий объект в self.

self возникает тогда, когда мы на основании класса создаём отдельный объект. этот объект наследует структуру и все возможности класса. И вот тот объект будет идентифицироваться через self, когда мы методы на него направляем.Все фрагменты логики, методы чаще всего, которые мы проэктируем для будующих объектов мы можем привязать к парковочному месту называющемуся стандартно self. И тогда пайтон поймёт, что в момент когда срабатывает эта логика, сюда должен быть припаркован объект с которым эта логика работает. 
self это как обратная ссылка на объект.
Классы находятся в прошлом относительно объектов класса. И поэтому в момент когда выполняется код связанный с объектом в будующем, код класса написанный в прошлом имеет доступ к этим объектам через self.

class Product:
 def __init__(self, name, price, rating):
  self.name = name
  self.price = price
  self.rating = rating
 def __str__(self):
  return f'-= PRODUCT ("{self.name}" {self.price}$ {self.rating}) =-'
 def __gt__(self, other):
  return self.rating > other.rating
 def __lt__(self, other):
  return self.rating < other.rating
  
p1 = Product("Programming book", 100, 4.5)
p2 = Product("Hacking book", 150, 5.0)
  
if p1 > p2:
 print("First book is better")
elif p1 < p2:
  print("Second book is better")
  
print(p1)
print(p2)