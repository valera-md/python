# intro.py
class Player:
 pass
def newPlayer(name, hp, avatar):
 player = Player()
 player.name = name
 player.hp = hp
 player.avatar = avatar
 return player
def printPlayer(player):
 print(player.name, player.hp, player.avatar)
p1 = newPlayer("Kinguru99",70,"kingu.gif")
p2 = newPlayer("Tigr",100,"t.gif")
printPlayer(p1)
printPlayer(p2)

# hm2:
# create class food, function newFood(name, price, quantity, weight)
# create class Drink, function newDrink(name, price, quantity, volume)
# create functions printFood(food), printDrink(drink) - format STRING * FEATURE: 
# create universal function printItem(item) * type
# if + else -> printFood()
# if + else -> printDrink()

class Food:
 pass
def newFood(name, price, quantity, weight):
 food = Food()
 food.name = name
 food.price = price
 food.quantity = quantity
 food.weight = weight
 return food
def printFood(food):
 print(f"{food.name} - {food.price} dollars, {food.quantity} portions, {food.weight} grams.")

class Drink:
 pass
def newDrink(name, price, quantity, volume):
 drink = Drink()
 drink.name = name
 drink.price = price
 drink.quantity = quantity
 drink.volume = volume
 return drink
def printDrink(drink):
 print(f"{drink.name} - {drink.price} dollars, {drink.quantity} cups, {drink.volume} liters.")
 
dish = newFood("Salad", 5, 1, 400)
printFood(dish)
drink = newDrink("Juice", 3, 2, 0.3)
printDrink(drink)

def printItem(item):
 if isinstance(item, Player):
  printPlayer(item)
 elif isinstance(item, Food):
  printFood(item)
 elif isinstance(item, Drink):
  printDrink(item)

printItem(p1)
printItem(p2)
printItem(dish)
printItem(drink)