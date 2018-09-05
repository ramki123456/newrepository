'''iterators: iterator is which can store group of values in the format of an object.
to create an iterator in python we will use iter method. 
iter method takes exactly one parameter that is any datastructure.
to access the data from iterator we will use next method.
next method will return the value at next iterator.
this method does not req any parameter.
the scope of next method is very limited due to causing of stop iteration error.
we can not control iteration behaviour in python so python developers introduced generator concept.
syntax: iter()
l = [1,2,3]
x=iter(l)
print x.next()
print x.next()
print x.next()
print x.next()

generators(): a generator is also an iterator which stores group of elements which results by condition.
to create a generator we will use the combination a function along with yield keyword.
when the yield keyword occur for first time python will create a generator object and the value after 
the yield statement will append to the generator object.

yield = data injection + return

note: we can control the iteration behaviour by using generator concept.

ex: def even(l):
	for i in l:
		if i%2==o:
			yield i
op = even(range(100))
print op

decorators(): a decorator is a wrapper function which will declare on top of any python function.
the decorator function name should preceded with @ symbol.
a decorator function will take the main function_name as a input.
whenever the main function called then python will excute decorator function, based on output of 
decorator the main function will excute.