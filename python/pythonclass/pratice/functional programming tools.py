'''functional programming tools:- functional programming tools are used to avoid the complexity of loops.
python provides 4 types of functional programming tools which are responsible for performing particular task.

1. filter 2. map 3. reduce 4. zip

1.filter: this method is used to perform only filtering operations this method takes exactly two parameters.
first parameter is function_name, group of elements.
filter method takes one element from group of elements at a time and calls the given function.
so the function defination should only one parameter.
filter method itself creates a list, perform the looping operations internally and appends the function returned data to the output list.
the output format is always given data structure.

syntax: filer(function_name, group of elements)

def function_name(element):
	-------------
	-------------

ex:'''

'''def even(a):
	if a%2 == 0:
		return a
print filter(even, (range(100))'''

'''map:- this method is used to perform manipulation operation on each and every element of given data structure
the output format is always a list. map method takes exactly two parameters just like filter.

syntax: map(function_name, group of elements)'''

'''def add(a):
	return a+3
print map(add, tuple(range(100)))'''

'''reduce:- this method is used to perform manipulation operation on all the elements of given datastructure.
this method takes exactly two parameters just like filter and map methods.
unlike filter and map reduce method will send two parameters.
the output format is always single element.
element can be of anytype.'''

'''def add(a,b):
	return a+b
print reduce(add, range(1,10))'''

'''zip:- this method is used to create list of tuples created from given datastructure.
this method takes exactly two parameters they are two data structures.
output format is always list of tuples.
syntax:zip(l1,l2)

note: to convert list tuples into  a dictionary use the inbuilt methods named as dict.
dict method takes exactly one parameter '''

print zip(['a','b','c'], [1,2,3])
print dict(zip(['a','b','c'], [1,2,3]))
