################################Lists ###########################

#Lists : Group of elements which are enclosed by two square brackets "[lists]" is known as a list in python.
#       Elements are seperated by ' , ' .
#        Elements can be any type(datatype or datastructures)
#      Lists are mutalble datastructures we can perfor CRUD operatoin(Create, Read, Update, Delete)
#      Lists are ordered datastructure so we can perform indexing and slicing to it.

#      Syntax : list_name = [element1, el1, etc...]

list_exam = ['one', 1.0, 1, [4]]
print list_exam


###### UPADATING AN Element in LISTS ####################

#update element : use below syntax to update an element in a list.

 #syntax : list_name[index] = value


list_exam[0] = 'Five'
print list_exam


############# Deleting an element in lists ################



del list_exam[0] 

print list_exam
########################## Methods To Lists

# 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'


################## append() ###########################
# .append()     : This method used to add one element at the end of the list.
# This method takes exactly one parameter i.e., element.
# The element can be of any type.

#            Syntax : list_name.append(25)

l = ['one', 1, 2, 2.0]
l.append(25)
print l


##################### insert() #########################
#.insert() : This method is used to insert an element at particular position.
#            This method takes exactly two parameters they are index position, element
#            This method will not return anything(None)
#            Element can be of any type.

#   Syntax : list_name.insert(0, 'bharath')

l.insert(0, [1,5])
print l

#.extend() : This method is used to insert multiple elements at the end of list.
#              this method will take exactly one parmeter i.e., group of elements (must be a datastructure)

# Syntax : list_name.extend("Datastructures")

l.extend("bharath")
print l # o/p : ['one', 1, 4.5, [2], 'b', 'h', 'a', 'r', 'a', 't', 'h']

print l.index('b') 

del l[4:]


#.pop() :  This method will return the element at given index position and then deletes it in list.
#            this  method will take at most one parameter i.e., index position.
#            If no parameters given this method takes ' -1 ' as default value.
#             O/p format is always an element.
           

           #     syntax : variable_name.pop(index_position)

l = [1,2,'bharath',3.5]
l.pop(2)# this element is deleted in the list.

# .remove(): This method is used to remove the given element from list.
#             This method takes exactyly one parameter i.e., element to delete.
#             The o/p format is always None.

#               Syntax : variable_name.remove(element)

    l = [1,2,'bharath',3.5]  
    l.remove('bharath') # 'bharath' element in list is deleted .

 /n
/n

# .sort(): This method is used to arrange the elements of list in particular order.
#          This method takes at most one parameter i.e., (reverse = True/False)
#          If reverse = True than python will sort the list in descending order.
#          If no parameters given python will sort the list in ascending order.
#          O/p formt is always none.

#        Syntax: variable_name.sort()    # Make lists into Ascending order.
#                   or 
#                variable_name.sort(reverse = True) # make lists into descending order.

b = [1, 2 ,10, 5, 8, 0,6]
b.sort() 



# .reverse() : This method is used to reverse the elements of list.
#              No parameters required.
#              o/p format is always none.

#                 syntax : variable_name.reverse()

              l = [1, 2, 3.5, 4, '5', 'a', 'r', 's', 't']


################ List comprehensions ###################

cubes = [i**3for i in range(5)]

print cubes.



            








