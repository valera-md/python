# products.py
from math import ceil
# from os import system
# p_c | 0 + 2
# p_c | 2 + 2
# p_c | 4 + 2
products = [ # list > dict > str, float
{"name": "Salad", "price": 25.00}, # 0 < i
{ "name": "Soup", "price": 15.00}, # 1 < min_i index_a
{ "name": "Bread", "price": 5.00}, # 2
{ "name": "Pepper", "price": 50.00}, # 3 < index_b
{ "name": "Black Bread", "price": 5.00}, # 4
{ "name": "Pizza", "price": 100.00},
{ "name": "Aubergine", "price": 30.00}
]
# hm1: write algo find max
max_i = 0
for i in range(len(products)):
 if products[i]["price"] > products[max_i]["price"]:
  max_i = i
print(f'{max_i} > {products[max_i]["name"]:25} {products[max_i]["price"]:7}MDL')
# hm2: find by name
# pruduct_name = " ... "
# for .. in .. + if + break
product_name = "Pepper"
for i in products:
 if i["name"] == product_name:
  print(product_name)
  break
# hw3: finish paginator
# check limits
# < >
# add "[page current]"
# <... 100 [101] 102 ...>
# simple pagination
# list
# ---
# [1] 2 3
item_count = len(products)
page_current = 1
per_page = 2
pages_total = ceil(item_count / per_page)
while True:
 # system("clear")
 start_index = (page_current - 1) * per_page
 end_index = start_index + per_page
 for i in range(len(products)):
  if i >= start_index and i < end_index:
   print(f'{i} > {products[i]["name"]:25} {products[i]["price"]:7}MDL')
 print()
 for page in range(1, pages_total + 1):
  if page == page_current:
   print(f"[{page}]", end = " ")
  else:
   print(page, end = " ")
 print()
 dir = input("< >")
 if dir == ">" and page_current < pages_total:
  page_current += 1
 elif dir == "<" and page_current > 1:
  page_current -= 1
