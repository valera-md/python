# Students Database
# * data structures
# * functional programming
# * CRUD operations - create, read, update, delete
# * interactivity - взаимодействие с пользователем
# * libraries
# * using "pip"

import random
import os
from faker import Faker
# fake = Faker('ru')
fake = Faker()
stud_names = [] # str
stud_grades = [] # float
stud_years = [] # int
def genStudents(amount = 10):
 for i in range(amount):
  stud_names.append(fake.name())
  stud_years.append(random.randint(1,5))
  stud_grades.append(round(random.uniform(5.0, 10.0), 2)) # HW1: round values dd.xx
def printStudents():
 for i in range(len(stud_names)):
  # print(stud_names[i], stud_years[i], stud_grades[i])
  print("-" * 42)
  print(f"{stud_names[i]:30} | {stud_years[i]:2} | {stud_grades[i]}")
 print("-" * 42)
def addStudent():
 s_name = input("Enter new student name: ")
 s_year = int(input("Enter new student year: "))
 s_grade = float(input("Enter new student grade: "))
 stud_names.append(s_name)
 stud_years.append(s_year)
 stud_grades.append(s_grade)
def editStudent():
 s_name = input("Enter the name of the student to edit: ")
 s_index = -1
 for i in range(len(stud_names)):
  if stud_names[i] == s_name:
   s_index = i
   break
 if s_index >= 0:
  stud_years[s_index] = int(input(f"Enter new year for {stud_names[s_index]}: "))
  stud_grades[s_index] = float(input(f"Enter new grade for {stud_names[s_index]}: "))
def removeStudent():
 s_name = input("Enter the name of the student to delete: ")
 s_index = -1
 for i in range(len(stud_names)):
  if stud_names[i] == s_name:
   s_index = i
   break
 if s_index >= 0:
  stud_names.pop(s_index)
  stud_years.pop(s_index)
  stud_grades.pop(s_index)
def bestStudent():
 max_value = max(stud_grades)
 for i in range(len(stud_grades)):
  if stud_grades[i] == max_value:
   print("-" * 42)
   print(f"{stud_names[i]:30} | {stud_years[i]:2} | {stud_grades[i]}")
 print("-" * 42)
def gradeRange():
 min, max = map(int, input("Enter minimum and maximum number separated by a space").split())
 for i in range(len(stud_grades)):
  if min <= stud_grades[i] <= max:
   print("-" * 42)
   print(f"{stud_names[i]:30} | {stud_years[i]:2} | {stud_grades[i]}")
 print("-" * 42)
def printMenu():
 print("### STUDENTS DATABASE ###")
 print("1. Show students list")
 print("2. Add a student")
 print("3. Edit a student")
 print("4. Remove a student")
 print("5. Find the best student(s)")
 print("6. Show all students within a grade range")
 print("0. Exit")
 print("######################")
 option = int(input(">>> "))
 return option
genStudents(5)
while True:
 os.system("clear")
 option = printMenu()
 if option == 1:
  printStudents()
  input("hit enter to continue")
 elif option == 2:
  addStudent()
 elif option == 3:
  # hm2: finish the edit code
  # user -> student name
  # find by name
  # new grade / year
  editStudent()
 elif option == 4:
  removeStudent()
 elif option == 5:
  bestStudent()
  input("hit enter to continue")
 elif option == 6:
  gradeRange()
  input("hit enter to continue")
 elif option == 0:
  break
# hw3: 
# a. find the best student (find maximum value)
# b. show all students within a grade range (7 - 9)