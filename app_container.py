part1.md
OOP like PRO /part 1
- static
- class
- attributes (properties)

HWl: create the function "setContainerValue(...)" <- args:
1. the class reference
2. a new integer value
the function sets the value inside the class
NOTE: the function should update is_empty to False

HW2: create the function "unsetContainerValue(...)" <— args:
1. the class reference
the function sets the value inside the class to None
NOTE: the function should update is_empty to True

HW3: create the function "printContainerValue(...)" <— args:
1. the class reference
the function checks if the class Container is empty
if it's empty, it prints: "Container is empty"
if it has a value: "Container<123>"

app.py
# static usage of a class
class Container:
 value = None
 is_empty = True
#print(Container.is_empty)
#print(Container.value)

def setContainerValue(Class, value):
 Class.value = value
 Class.is_empty = False

def unsetContainerValue(Class):
 Class.value = None
 Class.is_empty = True

def printContainerValue(Class):
 if  Class.is_empty == True:
  print("Container is empty")
 elif Class.is_empty == False:
  print(f"Container<{Class.value}>")

setContainerValue(Container, 123)
printContainerValue(Container)
unsetContainerValue(Container)
printContainerValue(Container)
+--------------- main program -----------------------+
|                    call                            |
|                     |                              |
|class Container:    setContainerValue(Class, value) |
|                                       |       |    |
|                     +-----------------+       |    |
|                     v                         |    |
| value = None    <- Class.value = value    <---+    |
|                     v                              |
| is_empty = True <- Class.is_empty = False          |
+----------------------------------------------------+
+--------------- main program -----------------------+
|                     call                           |
|                      |                             |
|class Container:     unsetContainerValue(Class)     |
|                                          |         |
|                      +-------------------+         |
|                      v                             |
| value = 123      <- Class.value = none             |
|                      v                             |
| is_empty = False <- Class.is_empty = True          |
+----------------------------------------------------+
+--------------- main program ---------------------------------------+
|       call                                                         |
|        |                                                           |
|       printContainerValue(Class)                                   |
|                            | |                                     |
| +- Class.is_empty == True -+ +- Class.is_empty == False: -+        |
| v                                                         v        |
| print("Container is empty")     print(f"Container<{Class.value}>") |
|                                                                    |
+--------------------------------------------------------------------+