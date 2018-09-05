####################FUNCTIONS ######################
# The block of code which is used to perform particular task is known as a function.
#functions are reusable blocks which will invoke many times as needed.
#based on usage and creation functions are divided into two types.
# in-built or system define functions 
# user define functions.


# User Define Functons
# To create any function in python we will use a keyword named as "def"
#Every function is a combination of two sections they are called function and calling function
  #-> A function which contains def keyword, function name , set of parameters, set of statements along with 'return' keyword is known as called function.
  #  -> calling functions contains only name and set of statements only.

# Note: no called function will execute without calling function.

#syntax: def function_name(parameters):
#             statements
#             statements
#             retrun 
#        function_name(value)

#eg:-
"""def add(a,b):
   c = a + b
   return c
print add(5,6) """



#Note: The number of parameters passing to a function should equals to number of parameters receiving.
# python will take latest function and  it will make other functions as idle when we create multiple functions with same name.

# To avoid the above problem python developers introduced default parameters methodology.

############################DEFAULT PARAMETERS########################
# The parameter which doen't require the data from user is knwon as default parameters.
# Default parameters can define by using assignment operator.
#these parameters should place after the manditory parameters.
# These parameters are used to extend function accesability to some level.



#syntax: def function_name(parameters, default parameters):
#            statements
#            statements
#            return
#        print function_name(values)



"""def multiply(a,b,c=10,d=35):
    multi = a*c*(b*d)
    return multi
print multiply(1,2)
print multiply(1,2,3,4)"""


# To work with unknown number of parameters python developer introduced "*args" and "**kwargs"

###################################### (*args) #######################)
#here star represents a tuple which accepts unknown number of parameter. args is a variable name it can be any name.

'''def add(*a):
    return a

print add(range(10),range(10,20))'''



###################################### {**kwargs} ##############################################

# This parameter is used to accept unknown number of items.
# These items will be store in a dictionary format.
#While passing the itmes define a variable with some value using assignment operator.


"""def keyv(**a):

    print a

keyv(a=10,b=1,c=20)
keyv(a=1,b=1,c=1)"""



############################   parameter order ########################

# (Mandatory par, Default Par, *arg, **kwarg )


###################Task ##################


# write a function to return list of elements which are divded by 3 and 5.

def divided(list_value):
   for div_value in list_value:
      if div_value/3 == 0:
         return div_value
      elif div_value/5 == 0:
         return div_value
      else:
         return None
print divided((raw_input("enter number:"))
        




# a list name is scores = [ ('pak',96), ('Aus', 98), ('Aus',69), ('pak', 28), ('SA', 69), ('SA',298) ]
# get  highest  average country.

