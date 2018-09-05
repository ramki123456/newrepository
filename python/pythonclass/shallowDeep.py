#Shallow Copy ( Shadow copy): The process of copying the object of one variable to another variable is known as shallow copy.
# Shallow copy will be performed on all kinds of data types and data structrures.
# But Imutable objects will not obey the rules of shallow copying because of item assignment is not possible.
# Shallow copy on mutable objects.

#Eg:-  Mutable -> lists and 
      
      l1 = [1,2,3]
      l2 = l1
      l[1] = 20 # here o/p of l1 is [1,20,3]

# l2 parameters also got changed.

#
      
##############Deep Copy ############333333
# The process of copying entire data form one variable to another variable is known as deep copying.
# To perform deep copy in Ordered DataStructures we will use 'slicing operation'
# ON UNORDERED DATA STRUCTURES we can't use slicing rather we will use copy method to perform deep copy.

# Eg:-

         l1 = (1,2,3)
         l2 = l1[ : : ]





          
