'''What will be the output of the code below? Explain your answer.

def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3

The output of the above code will be:

list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a']

How would you modify the definition of extendList to produce the presumably desired behavior?

The definition of the extendList function could be modified as follows, though, to always begin a new list when no list argument is specified, 
which is more likely to have been the desired behavior:

def extendList(val, list=None):
  if list is None:
    list = []
  list.append(val)
  return list

With this revised implementation, the output would be:

list1 = [10]
list2 = [123, [1,2]]
list3 = ['a']

What will be the output of the code below? Explain your answer.

def multipliers():
  return [lambda x : i * x for i in range(4)]
    
print [m(2) for m in multipliers()]

How would you modify the definition of multipliers to produce the presumably desired behavior?

One solution would be use a Python generator as follows:

def multipliers():
  for i in range(4): yield lambda x : i * x 

Another solution is to create a closure that binds immediately to its arguments by using a default argument. For example:

def multipliers():
  return [lambda x, i=i : i * x for i in range(4)]

Or alternatively, you can use the functools.partial function:

from functools import partial
from operator import mul

def multipliers():
  return [partial(mul, i) for i in range(4)]

What will be the output of the code below? Explain your answer.

class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print Parent.x, Child1.x, Child2.x
Child1.x = 2
print Parent.x, Child1.x, Child2.x
Parent.x = 3
print Parent.x, Child1.x, Child2.x

The output of the above code will be:

1 1 1
1 2 1
3 2 3

What will be the output of the code below in Python 2? Explain your answer.

def div1(x,y):
    print "%s/%s = %s" % (x, y, x/y)
    
def div2(x,y):
    print "%s//%s = %s" % (x, y, x//y)

div1(5,2)
div1(5.,2)
div2(5,2)
div2(5.,2.)

In Python 2, the output of the above code will be:

5/2 = 2
5.0/2 = 2.5
5//2 = 2
5.0//2.0 = 2.0

What will be the output of the code below?

list = ['a', 'b', 'c', 'd', 'e']
print list[10:]

The above code will output [], and will not result in an IndexError.

Consider the following code snippet:

1. list = [ [ ] ] * 5
2. list  # output?
3. list[0].append(10)
4. list  # output?
5. list[1].append(20)
6. list  # output?
7. list.append(30)
8. list  # output?

The output will be as follows:

[[], [], [], [], []]
[[10], [10], [10], [10], [10]]
[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]

Given the following subclass of dictionary:

class DefaultDict(dict):
  def __missing__(self, key):
    return []

Will the code below work? Why or why not?

d = DefaultDict()
d['florp'] = 127

Yes, it will work. With this implementation of the DefaultDict class, whenever a key is missing, 
the instance of the dictionary will automatically be instantiated with a list.'''

'''class DefaultDict(dict):
  def __missing__(self, key):
    return []

Will the code below work? Why or why not?

d = DefaultDict()
d['florp'] = 127'''

l = [1, 2, 3, 4]
l.append([33, 4])
# op: [1,2,3,4,33,4] bcoz element can be any type that maybe datastructure
# or single element.

l.extend(15)
