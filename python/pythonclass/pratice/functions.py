 '''functions: the block of code which is used to perform particular task is known as function.
functions are reusable blocks which will invoke(calling) many times as needed.
based on usage and creation functions are divided into two types.

1. inbuilt/system defined 2.user defined

user defined functions: to craeate any functions in python we will use keyword def.
every function is a  combination of two sections they are called function and calling function.
a function which contain def keyword, function_name, set of paramerters, set of statements along with return statements
is known called statements.
calling function contains the function_name and set of parameters only.
note: no called function will execute without calling function.

syntax:-

def function_name(par1,par2):
	--------
	--------
	return
function_name(par1,par2)

Ex:-

def  add(a,b):
	c = a+b
	return c
print add(10,20)
print add(20,30)
print add(40,50)

note: the no of parameters passing to a function should equals to no of parameters receiving. 
to avoid the above problem python developers introduced default parameter methodology.

default parameters: the parameters which does not require the data from the user are known as default parmeter.
default parameters can defined by using assignment operator.
these parameters should place after the mandatory parameters.
these parameters are used to extend function accessability to some level.
to work with unknown no of parameters python developers introduced *args, **kwargs

*args: * represents a tuple which can access unknown no of parameters. args is a variable name it can be any type.
def add(*a):
	return sum(a)

**kwargs(key word args): this parameter is used to accept unknown no of items. 
these items store in dictionary format.
while passing items define a variable with value.

def add(**d):
	print d        #print sun(d.values)
#add(key1=val1, key2=val2)
add(a=10, b=20, c=30)


def add(a,b,c=0,d=10):
	return a+b+c+d
print add(10,20)
print add(40,60,70)
print add(90,40,20,10)

note: the life time of function variable is within a function.
print a,b

note: python will take latest function and it will make other function as idle when we create multiple functions with same name.'''

'''def add(*a):
	return sum(a)
print add(10)
print add(10,20)
print add(1,2,3)
 
parameters order:
(m.p, d.p, *args, **kwargs):
def add(a, b, c=0, d=0, *e)

write a function to return list of elements which are divided by 3 and 5.

score = [('pak', 96), ('aus', 98), ('aus', 69), ('pak', 28), ('sa', 69), ('sa', 298)]
find a avg and name of country.
