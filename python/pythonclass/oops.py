'''oops:- oops stands for object oriented programming structure.
is mainly used to create a particular structure of statements can be formed by grouping multiple python objects(int, tuple, dictionaries,list).
by using oops concepts we can provide security, extendability and reusability.
oops is built based on two major properties named as class and instance.

class:- class nothing but an entity which holds multiplae or group objects.
a class can be created by using 'class' keyword.

syntax: class Class_Name:
			set of objects.

instance:- an instance is reference to the class. by using instance we can access the properties of the class.

syntax: instance_name = Class_Name()

ex:

class Emp:
	sal = 10000
	time = 12
obj = Emp()
print obj.sal
print obj.time

note: while creating an instance to the class python will call __init__ __new__ and __methond__.
__init__ is known as a constructor. __new__ __method__ will always to create a new instance in separate memory location.
and predefined class we can insert the new properties directly (by using assignment operators) but to update or access or to delete any property the property should exist.


class A:
	x = 10
	y = 20
a = A()

print a.x
print a.y
print a.z = 20

placing functions in a class: the functions which lies in a class should contain self as first parameter.
here self is a keyword which nothing but an instance of the class.
an instance is reference of the class can access class data only from outside the class.
but self can use only from inside the class. technically self will work only from the functions of the class.

self = instance of the class.

while calling class based sentence python will send reference of the class as the first parameter to the approriate function there after function
will take ref and copy to ref self.


class Maths:
	def operation(self,a,b):
		self.a = a
		self.b = b
		return a+b, self.mul(), self.div()

	def mul(self):
		return self.a*self.b

	def div(self):
		return self.a/self.b

obj = Maths()
print obj.operation(10,20)'''

class A:
	def __init__(self,a,b):
		self.a = a
		self.b = b
		return self.add()
	def add(self):
		return self.a+self.b
	def mul(self):
		return self.a*self.b
obj = A(10,20)

'''constructor: is a function which will invoke automatically when an obj(instance) created for given class.
in python __init__ function is treated as constructor.
the return type of constructor is always none.
to pass the data to a constructor use class instance creation.'''