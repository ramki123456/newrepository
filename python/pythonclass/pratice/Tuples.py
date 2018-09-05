#Tuples(): the group of elements which are enclosed between two paranthesis is known as Tuples
#	here elements are separated by comma 
#	Tuples are ordered data structures so we can perform index and slicing.
#	tuples are immutable datastructures so we can't perform modification operations.
#syntax: tuple_name=(element1,element2)
#	theoritically we can't modify tuples but in special situations like placing mutable objects we can modify a tuples

t=(1,2,[3,4],5)
t[1]=10				#will not support
t[2]=15				#will not support
t[2][1]=20
print t
