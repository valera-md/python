# FUNCTIONAL like PRO / part 4
# square-in-out.py
# Square(value) ---> value ^ 2

# 1. classic solution (args-IN,return-OUT)
def square(value):
 # result = value * value 
# HW1: find other methods of obtaining square number (min 2 var)
 # result = value ** 2
 result = pow(value, 2)
 return result
n = 10
n = square(n)
print(n)

# 2. alternative solution (args-IN,OUT)
def square(value):
# variant 1
 # value[0] = value[0] * value[0]
# variant 2
 # res = value[0] * value[0]
 # value.pop(0)
 # value.insert(0, res)
# variant 3
 value.append(value[0] * value[0])
 value.pop(0)
n = [10]
square(n)
print(n)

# hm2: create a function (generalMark) which receives 3 numbers from a dictionary, draw the diagram
IN {
"sem_1": 9.0,
"sem_2": 8.0,
"exam":  8.0,
}
OUT {
"sem_1": 9.0,
"sem_2": 8.0,
"exam":  8.0,
"gen":   8.33...
}

def generalMark(value):
 value["gen"] = round(sum(value.values()) / len(value), 2)
marks = {"sem_1": 9.0, "sem_2": 8.0, "exam":  8.0}
generalMark(marks)
print(marks)

diagram
        marks ~> ["sem_1", ... ] dictionary
        |    ^ \  
        |    |  -------------------------------------
        v    |                                       \
generalMark(value)|                                   \
        |   /                                          \
        v  /                                            \
       value                                             \
        .                                                 \
value["sem_1", ... ] -> read -> original                   \
        |                                                   \
        v                                                    v
value["gen"] = round(sum(value.values()) / len(value), 2) --> 8.33
