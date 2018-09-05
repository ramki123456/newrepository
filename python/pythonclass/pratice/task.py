
cities = ['bangalore,', 'chennai', 'hyderabad', 'tirupati', 'goa', 'pune', 'maharasta']
def place(name):
	if len(name)<6:
		return name
print filter(place, cities)