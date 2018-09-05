################## Functional Programming Tools #####################
#Functional programming tools are used to avoid the complexity of looping.
#Python provides ' 4 ' types of functional programming tools which are responsible for performing particular task.
# 1.filter
# 2.map
# 3.reduce
# 4.zip


############### filter #################

# This method is used to perform only filtering operations.
# This method takes exactly two parameters first parameter is a function name and second parameter is group of elements.
#filter method takes one element form group of elements and calls the given function,So the function def should contain only one parameter.
#filter method itself creates a list, perform the looping opertaion internally and appends the function returned data to the list.
#The o/p format is always given datastructure.


# Normal Loop 
def even(list1):
    l1 = []
    for ele in list1:
         if ele % 2 == 0:
            l1.append(ele)
    return l1
print even(range(100))

# Now we use filter method.

# syntax :  def function_name(one parameter):
#               if condtion:
#


#     filter(function_name, groupofelements)

def even(a):
   if a%2 == 0:
     return a
print  filter(even, range(100)) # here range(value) return in lists
print filter(even, tuple(range(100)))

#eg2:

def name(cities):
     if len(cities)<=6:
        return cities
print filter(name, ['Banglore', 'Chenni', 'Goa', 'Pune', 'Hyderabad'])



############### map ####################

#This method is used to perform manipulation operation on each  element of given datastructure.
# The o/p format is always a list.
# map method takes exactly two parameters just like filter.
# map method takes one element form group of elements and calls the given function,So the function def should contain only one parameter.
#eg:-


def adding(cities):
        return cities + ' Is my home town'
print map(adding, ['Banglore', 'Chenni', 'Goa', 'Pune', 'Hyderabad'])
print map(adding, ('one', 'two', 'three', 'four', 'five'))



############## reduce ####################

#This method is used to perform manipulation operation on all the  element of given datastructure.
#This method takes exactly two parameters just like filter and map methods.
#Unlike filter and map reduce method will send  two parameters to the given function.
# The o/p will get only single element that can be any type.


def add(a,b):
    return a + b
print reduce(add, range(100))


#################  zip #####################
#This method is used to create  list of tuples created form given datastructures.
#This method takes exactly two parameters they are two datastructures.
#o/p format is always  list of tuples.

# syntax :  zip([l1],[l2])


print zip(['bharath','ramkrishna','siva','basha','cheru'], [27,25,23,23,25])
#Note : To convert list of tuples into a dictinory use the inbuilt method named as dict.

#dict() takes exactly one parameters.

print dict(zip(['bharath','ramkrishna','siva','basha','cheru'], [27,25,23,23,25]))






