############ List comprehensions ##############################
# list comprehension is a consise or easiest way to create complex data list.
# list comprehension is one line statement.
# A list comprehension should enclose between squeare brackets.
# It contains three major sections they are 
  # 1. operation section
  # 2. Looping section
  # 3. Condition Section(optional)

# Syntax : [ operation/variable        looping       conditionalstatements(optional)]




########### syntax for if else conditon with list comrehe #################

# we can include negative conditonal scenorios in list comprehension by using below syntax.

#    syntax : [ op1  if condition else op2  looping]



print [sal+sal*0.10 if sal<5000 else sal  for sal in range(2000,20000,1000)]
