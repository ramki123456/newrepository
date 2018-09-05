'''lambda functions: lambda functions are one line functions in python which can be created by using lambda keyword.
lambda functions does not contain return statement the scope of lambda functions are very limited.
due to unaccessability of multiline and multiparameters.

syntax: function_name = lambda parameters: operations

add = lambda a,b: a+b
print add(10,20)

using lambda functions along with ftp.'''

ex: print filter(lambda a: a%2==0, range(100))

print filter(lambda name: name.startswith('R'), ['hari', 'ravi', 'raju'])

salaries = [5000,6000,4500,8000,9000]

op_list = filter(lambda salaries: salaries>5000, salaries)
print reduce(lambda a,b: a+b, op_list)

print reduce(lambda a,b:a+b, filter(lambda salaries: salaries>6000, salaries))

