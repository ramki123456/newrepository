############################ LOOPS #########################################
# Executing same set of statements for multiple times is known as looping.
# looping is also known as 'iteration'
# Python supports two types of looping mechanisms they are
# for - 1oop, While-loop

################ for ##########################################
# In python for loop doesn't require item assignment, conditonal formatting and incriment or decriment operator.
# A for loop can be built based on the combination of for and in keywords.
# for loop will take one value from given group of elements and assign to given variabl.
# The above process will be repeated for len(group of elements times).

# syntax : 
 #          for variable in group of elements:
                #statements.
                #statements.
                #statements.


'''l = [1,2,3,4,5,6,7,8,9,10]

for i in l:
    print i

for i in l:
   if i%2 == 0:
     print i
   elif i%2 != 0:
      print i'''

# Note : In python " for "  loops will use widely when compare with other looping machanisms because of high and reliable performance.
# break: break keyword can only used in for loop 
#        whenever break statement availble than python will come out of the loop and skip remaining interations.


l = [1,3,4,5,7]

'''for i in l:
    i%2 == 0
    print "list is invalid"
    break'''

for  i in l:
   print "checking",i
   if i%2 == 0:
      print "list is invalid"
      break

#Continue: Continue is a keyword which is used to skip the current itteration and start new iteration.
#          This keyword should place inside the for loop.

'''for i in l:
       if i%2 !=0:
          continue
          print "Odd number",'''


#membership operator: These operators are used to check the availability of an element in group of elements.
# Python provides two types of memebership operators they are 
                    # in  
                    # not in 
# in : it will return true only if an element available in group of element.
# not in : it will return true only if an element not  available in group of element.

# The output of memebership operatior is always a boolean operator.





                




