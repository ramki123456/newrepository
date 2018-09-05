############ iter() iterators  method ##############
# iterator is just a container which can store group of values in the format of objects(iterator object)
# to create an iterator in python we will use method -> iter()  
# method  iter() takes exactly one parameter i.e., any data structure.
#To access the data from interator we will use next method 
#Next method will return the value at next iteration and this method doen't require any parameter.
# The scope of next method is very limited due to causing of stop iteraion error.
# we can't control iteraton behaviour in python so python developers introduced generators concepts.
x = iter(range(2))
print x.next()
print x.next()
print x.next()
