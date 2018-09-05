###############LAMBDA FUNCTIONS ###################
# Lambda functions are online functions in python which can be created by using lambada keyword.
# Lambda function doesn't contains return statement.
# The scope of Lambda functions are very limited due to unaccesability of multiline and multiparameter mechanism.

#     syntax : function_name = lambda parameters/varaibles: operation 
#               print function_name(parameter values)

#     Exam :    
multiply     = lambda  one,two :  one*two
print multiply(2,5)


add = lambda a,b: a +b
print add(10,20)


#### Using Lambda with function along with filters

print filter(lambda a: a%2==0, range(100)) # here we use filter method
print reduce(lambda a,b: a+b, range(5,20,5) # here we use reduce method







