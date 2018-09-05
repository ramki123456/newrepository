#pop():- this method will return the element at given index position and then deletes it.
#	this method takes at most one parameter that is index position 
#	if no parameter given this method takes -1 as default value.
#	the output is always an element.
#syntax: list_name.pop(index position)
l=[1,2,3,4]
print l.pop(2)
print l
print l.pop()
print l

#remove():- this method is used to remove the given element from the list.
#	this method takes exactly one parameter that is element to delete.
#	the output format is always none
#syntax: list_name.remove(element)
l=[1,2,3,4]
l.remove(3)
print l

#sort():- this method is used to arrange the elements of the list in particular order.
#	this method takes atmost one parameter(reverse=True/False)
#	if reverse=True then python will sort the list in descending order.
#	if reverse=False then python will sort the list in ascending order.
#	if no paramenters given python will sort in ascending order
#syntax: list_name.sort(reverse=True)	#for decending order
l=[1,4,2,3,0]
l.sort()
print l
l.sort(reverse=True)
print l

#reverse(): this method is used to reverse the given list.
#	no paramenters required 
#	the output format is always none
#syntax: list.name.reverse()
l=[3,1,4,2,6]
l.reverse()
print l
