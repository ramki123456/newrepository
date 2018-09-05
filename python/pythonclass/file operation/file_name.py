#read:to work on read operation mode use open method along with file name and r as operation mode.open method will return if file object as o/p which holds the data in given file.
#read method will return the complete file data in the form of string.this method accepts atleast 0 parameter atmost one parameter.if yoyu are not passing any parameter it will return all the character of the file.if you are passing an integer as a parameter then it will reteurn given no.of characters 
#syntax:file_pointer_variable.read(integer(optional))
#example:
#print open('some')
fp=open('some')
#print dir(fp)
#print len(fp.read()),'no ofcharacters'
#print fp.readline()
#readline:this method will return the first line data of given file.this method accepts atmost oneparameter i.e integer.if you are passing an interger then it will return given no;of characters of interger.
#syntax:filepointer_name.readline(int(optional))
#readlines:this method will return list of all the lines of given file.each and every element in the list ends with \n.
#syntax:filepointer_name.readlines()
k=len(fp.readlines()),'no of lines'
print k
#close: this method is used to remove from file pointer(it remove from memory)
#filepointer_name.close()
#example:fp.close()
fp.seek(0)
print "No of words", len(fp.read().split())
#iterators:iterators are containers which holds group of elements in an object format.the object name will contain iterator keyword.
#to create an iterator will we use iter() method.
#syntax:iterator_name=iter(d.s)
#use next ()method to acces the datafrom iterator.
#syntax:iterator_name.next().no parameter required.
#note:next method will return 'stop iteration error if no element or left iterator'.we can control iteration behavor as no condtions will applyon iterble data.
x=iter([1,2,3,4,5])
print x
#print x.next()
for i in x:
    print i
#genarator:to avoid the problem caused by iterators use genarators.every genarator is an iterator but not viceversa.genators are an object which holds conditional formated data.
#use a function along with yeild keyword.the genarator name willbe the function name.
#syntax:def genarator(data):
#              yeild
#              print genarator()
def even(l):
	for i in l:
		if i%2==0:
			yield i
print even([1,2,3,4])
def even(l):
	yield[i for i in l if i%2==0]
o=even(range(10))
print o
print o.next()
#decorators:these are wrapper functions in python which holds another function.decorator function will take the another function name(function object)as a parameter.
#a decorator function should declare on top of any function by declaring the decoring function on top of main function which preceded by '@' symbol.
#syntax:@decorator_name
#          def function_name(*args)
#if we are calling main function the decoration function execute.
#syntax for defining decorator:def decorator_name(function_name):
#                               def wrapper(*args):
#                               #operation,#return sum data,#if success,#call main function
#                                 function_name(*args)
#example:class method,static method,login method..........
'''@ decorator()
def add(a,b):
	return a+b
print add(10,20)'''
#modules:a modules is a container which holds requred data in the form of oython objects(every thing in python is a module)every python file willbe treated as module.
#modules mainly implemented for achiveing modularity machanism(accesing the existing data in some otherfile).the main purpose of modules is reusabulity.
#types of modules:python supports 3 types of modules they are 1)user defined2)systen inbulit(internal)3)thrid party(eternal)
#userdefined:the modules which are created by user are known as user defined modules.to access module datav in another files python provides 2 machanisms they are import and from-import.
#import:this keyword is used to acceess higher or outer level data available inmodule.using importstatement all the sub functionality or sub level dataoccupy othe memory in python.
#syntax:import module name
#to access sublevel functionality use '.'symbol.
#ex:import test.add(10,20)
#note:import statement on higher level data will cause higher memory consumption python allocate memory for sub functionality.to over come these senario we can use from-import statement.
#from-import:
#sytax:from outerlevel import innerlevel
#example:from test import add.....from test import add, mul.......from test import *(import entire)
#system inbuilt modules:1)datetime2)os3)sys4)json5)xml6)math7)collection9)urllib10)steptools11)socket12)subclasses133)csv14)html)15)itertools16)smtplib17)email....................etc
#datetime:to work with date and time object
#os:to work on os commands
#sys:system driver command.
#numpy:for advance d.s.
import math
print dir(math)
print math.sqrt(25)
import datetime
print datetime.datetime.now()
#thrid :the modules which are not available in systen and not created by use are known as thrid party module(created neigher by user or python)thrid module available in dynamic or internet.
#examples:xlrd,xlwt,paypol,twilio,django,request(in some versions only),opencafe,mysqldb,pycong2,oauth,auth0,oracle........etc