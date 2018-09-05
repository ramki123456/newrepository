########### Module Usage  ##################
# Python provide two mechanisms to access the data from modules .
   # they are   1. import    2. from - import

# import :-
          # import statement/keyword is used to dump all the functions and objects  from other python file.
          # use the name which declare after the import statement.
 
                 # syntax : import module_name
               
import test
print test.get_sum([1,2,3,4,5])


                            # ************ NOTE ******************* #
# The scope of import statement is limited because of higher memory conception.
         

# form-import:-
                # from-import is a combination of two keywords they are from and import.
                # After the from keyword we should specify the higher level module name(package name).
                # we should mention the function name to be used after import keyword.
                # form-import mechanism is used to dump the required functionality into the memory.
                    
                      # syntax: from  module/package  import  function_name

from test import get_even
print get_even([1,3,5,6,8,10,12])

                # The above syntax is used to import only one function.
                # use below syntax for multifunction import.

                      # syntax: from module/package import function_name1,function_name2,.....



                # use below syntax to use all the functions of particular file.
                           
                        #syntax : from module/package import *
from test import *

print get_even(range(10))




   
