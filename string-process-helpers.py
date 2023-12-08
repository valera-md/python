# string-process-helpers.py
# str (string) < methods

def removeSpace(name):
 name_ = name.strip()
 return name_

def fixCase(name):
 name_ = name.capitalize()
 return name_

# correct_name = removeSpace(' Dorin ')
# correct_name = fixCase(' dOrin ')
# hm1: refactor the code bellow -> pass value through a variable 
correct_name = fixCase(removeSpace(' dOrin '))
print (f"|{correct_name}|")
without_spaces = removeSpace(' dOrin ')
capilalized_name = fixCase(without_spaces)
print (f"|{capilalized_name}|")