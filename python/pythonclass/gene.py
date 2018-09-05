######### Generators yield keyword ############
# A generator is also an iterator which stores group of elements which results by a condition.
# To create a generator we will use the combination of a function along with yield keyword.
# 1. when the yield keyword occurs for first time python will create a generator object and the value after the yield statement will append to generator.
# 2. Yield is a combination of data insertion process and return statement.

# NOTE : we can control the iteration behaviour by using generator concept.

'''
def eve(l):
   for i in l:
       if i%2==0:
         yield i
op = eve(range(100))
print op
print op.next()

'''
l = [1, 2, 3, 4]
l.append([33, 4])
print l
l.extend([1,2,5])
print l