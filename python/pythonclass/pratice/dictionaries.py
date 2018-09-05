'''#dictionaries:- the group of items which are enclosed by two {} are known as dictionaries.
	in dictionaries items are separated by comma.
	an item is a combination of key and value fair. key and value separated by :
	dictionaries are mutable datastructures so we can modify a dictionary.
	syntax: dictionary_name={item1,item2,------}	item: key+value
	dictionary_name={key1:val1, key2:val2}
	in dictionaries keys are unique and should accept immutable data only.
	immutable-(int, float, )
	in dictionaries values can be of any type and they do not contain 
	dictionaries are unordered datastructures which uses heap as memory unit.
	note: the datastructures from which we can not access data by using indexing process are known as unordered.
	unordered datastructures like dictionaries will  perform data manifulation operations very faster compared to ordered datastructures.
	dictionaries uses hashkey maechanism process (key paired with value) which will make data operations very faster.
	in dictionaries we can use a process named as keying which is used to access the data. 
	use below syntax to perform keying.

	syntax: dictionary_name[key]

	d = {'a':1, 'b':2, 'c':3}
	print d[a]

#updating an item: to update an item the key should exit in dictionary. 
follow the below syntax to update an element
dictionary_name[key]=value
d['c']=15
print d

to insert an item the key could not exit.
dictionary_name[key]=value
d['x']=20
print d

deleting an item:
syntax: del dictionary_name[key]
note: if you are inserting multiple val with same name dictionary crate an item with one key mapped with latest val.

d = {'a':1, 'b':4, c:'23', 'a':43}
print d

employee={1179:{'name':'hari', 'age':26, 'comp':['ibm, hcl, tcs'], 'loc':'banglore'}, 
		1180:{'name':'ravi', 'age':23, 'comp':['ibm, hcl'], 'loc':'chennai'}}

