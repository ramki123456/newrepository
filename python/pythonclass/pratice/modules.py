'''modules:- modules nothing but group of objects which are enclosed in a python file.
modules are divided into 3 types they are

1.inbuilt modules:  the modules which comes with default python version are known inbuilt modules.
ex: os, sys, datetime, time, csv, numpy, re, requests, urllib, urllib2, collections



2.user defined modules: the modules which are defined by the user known as user defiened modules.

3.third party modules: the modules which are not created by user and not as inbuilt, which are available in internet
known as third party modules.

usage:- python provides two mechanisms to access the data from modules they are

1.import: import statement(keyword) is used to dump all the functions and objects from other python file.
use the name which declare after import statement.
syntax: import module_name

ex: import text
print get_even([1,2,3,4,5,6])

l = [1,2,3,4,5,6]

def get_even(l):
	return filter(lambda a: a%2==0, l)

def get_sum(l):
	return reduce(lambda a,b:a+b, l)

def get_mul(l):
	return reduce(lambda a,b:a*b, l)
note: the scope of import statement is limited because of higher memory consumption


from-import(): is a combination of two keywords they are from and import.
after the from keyword we should specify the higher level module name or package name and 
we should mention function_name after import statement.
from-import mechanism is used to dump the require functionality into the memory.

syntax: from module/package import function_name

the above syntax is used to import only one funticon.
use below syntax for multi funticon import

syntax: from module/package import function1, funticon2, funticon3

use the below syntax to import all properties of particular file

syntax: from module/package import *

package:- package is a python container(folder) whcich can hold python files and folders.
to convert a normal folder to package place __init__.py inside the folder.
complete project details should place within a folder that folder is known project folder.


