# todo.list.py
# data
tasks = [
"Learn Python", # 0
"Become a DEV", # 1
"Become a MILLIONAIRE! :D", # 2
"Be mega happy!", # 3
"Learn Machine Learning" # 4
]
while True:
# interaction
 item = int(input("choose an item\n1. add task\n2. show tasks\n3. remove task\n4. clear todo\n0. exit"))
 if item == 1:
  new_task = input("Add task: ")
  if new_task not in tasks:
   tasks.append(new_task)
  else:
   print("This task already exists.")
 elif item == 2:
# print the tasks
  print("TODO list (", len(tasks), "):")
  for i in range(len(tasks)):
   print("\t", i, ">", tasks[i])
 elif item == 3:
  pos = int(input("what position ? "))
  tasks.pop(pos)
 elif item == 4:
  tasks.clear()
 elif item == 0:
  break