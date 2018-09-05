'''#Dictionary functions:-
1.keys: this method will return list of keys from given Dictionary.
	no parameters required. output format is always a list.
syntax: dict_name.keys()
ex: print d.keys()

2.value:- this method will return list of values from given Dictionary
	no parameters required. output format is always a list.
syntax: dict_name.values()
ex: print d.values()

3.items: this method will return list of items and each item lies in tuple.
	no parameters required. output format is always a list.
	syntax: dict_name.items()
	ex: print d.items()

4.viewkeys:- this method will return list of  keys in format of dict_keys_method
	no par req. output format is always list.
	syntax: dict_name.keys(['a', 'b', 'c'])
	ex: print d.keys()
5.viewvalues:- this method will return list of  val in format of dict_keys_method
	no par req. output format is always list.
	syntax: dict_name.keys([1, 2, 3])
	ex: print d.viewvalues()


#iterkeys: this method will return list of keys from given Dictionary in format Dictionary key iterator.
syntax:iterator(iteration)
dict_name.iterkeys()
#itervalues: this method will return list of values from given Dictionary in format Dictionary key iterator.
syntax:iterator(iteration)
dict_name.itervalues()
#iteritems: this method will return list of items from given Dictionary in format Dictionary key iterator.
syntax:iterator(iteration)
dict_name.iterkeys()


get: this method will the value at given key in Dictionary.
	this method takes atleast one parameter and at most two parameters.
	first par represents key and it is mandatory.
	second par represents value and it is value. and if u r not passing any value python will assign None by default.
syntax: dict_name[key]
d = {'a':1, 'b':2, 'c':3}
print d.get('a')
print d.get('x')
print d.get('x', 15)
print d.get('a', 10)

note: this method will return value at given key if key is available and this method will return second parameter only if key is not available.

setdefault: this method will work just like get method when the key  is available in Dictionary this method will insert and item when key is not available.
	(first it will return the value and then do the certain operation based )
	first par represents key and it is mandatory.
	second par represents value and it is value. and if u r not passing any value python will assign None by default.
syntax: dict_name[key]
d = {'a':1, 'b':2, 'c':3}
print d.setdefault('a', 100)
print d
print d.setdefault('y',100)
print d

pop:- this method will return the value at given key and then deletes the particular item.
	this method takes atleast one parameter and atmost two parameter
	first par represents key and it is mandatory.
	second par represents value and it is value. and if u r not passing any value python will assign None by default.
syntax: dictionary_name.pop(key, value)
d = {'a':1, 'b':2, 'c':3}
d.pop('a')
d.pop('x')

popitem(): this method will always return first item of the dictionary and then deletes it.
	no parameters req. output format is always tuple.
syntax: dictionary_name.popitem()
d = {'a':1, 'b':2, 'c':3}
print d.popitem()
print d

has_key:- this method will return True if the key is available in dictionary or else it will return false.
	this method takes exactly one parameter that is boolean operator.
syntax: dictionary_name.has_key(key)
print d.has_key('a')
print d.has_key('x')

clear: this method will deletes all the data of given dictionary. no par req. 
	it will not return anything.
	dictionary_name.clear()
d.clear()
print d'''