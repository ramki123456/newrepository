'''def even(a):
	if a%2 == 0:
		return a
print filter(even,range(100))'''

cities = ['bangalore,', 'chennai', 'hyderabad', 'tirupati', 'goa', 'pune', 'maharasta']

'''def place(a):
	if len(a)<6:
		return a
print filter(place,cities)'''

def add(a):
	return a+2
print map(add, tuple(range(1,10))

'''print zip(['a','b','c'], [1,2,3])
print dict(zip(['a','b','c'], [1,2,3]))'''