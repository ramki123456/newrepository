#list:- group of elements which are enclosed by [] is known as a list in python. elements are separated by , . element can be of any type either datatype or data structure.
#list is mutable data structure so that we can perform CRUD operations
#c-create, r=read/insert, u=update, d=delete
#list is ordered data structure so that we can perform indexing and slicing 
#syntax: list_name=[element1, element2,-----]
l=[1, 2, 3.0, 'hello', [4,5]]
print l[3]
print l[3][1]
print l[4][1]
print l[:3]

#update:- To update an element use below syntax to update an element in a list
#syntax:- list_name[index position] = value
l[2] = 10
print l

#delete:- 
#syntax:- del list_name[index postion]
l=[2,3,4,5]
l.del[2]
print l

#append:- this method is used to add one element at the end of the list. this method takes exactly one parameter that is an element. the element can be of any type. 
#syntax:- list_name.append(element1)
l=[1,2,3,4]
l.append(5)
print l
l.append([5,6])
print l

#insert:- this method is used to inseert an element at particular position. this mehod takes exactly two parameters they are index position, element. this method will not return anything(None).
#element can be of any type.
#syntax:- list_name.insert(index position, element)
l=[1,2,3]
l.insert(1, 10)
print l
l.insert(0, [1,5])
print l

#extend:- this method is used to insert multiple elements at end of the list.
#this method takes exactly one parameter that is group of elements(must be a data structure)
#syntax: list_name.extend(data structure)
l=[3,4]
l.extend([5,6])
print l
l.extend("hi")
print l