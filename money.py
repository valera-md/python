# money.py
class Money:
 def __init__(self, amount, currency):
  self.amount = amount
  self.currency = currency
 def __str__(self):
  return f"{self.amount:5} {self.currency:3}"
 def __sub__(self, other):
  return Money(self.amount - other.amount, self.currency)
salary = Money(1000,"EUR")
expence = Money(300,"EUR")
print(salary)
print(expence)
rest = salary - expence
print(rest)