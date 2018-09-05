# dir(): This method will return list of functions which can perform on given variable.
#1.This method takes exactly one parameter i.e, variable name.
     
#syntax : dir(variable_name)

my_name = "Bharath"
print dir(my_name)


#######################################String Methods:##########################################

#str.catpitalize(): This method will return first letter Capital.
#This method doesn't require any parameters.
#O/p format is always a string.

#Syntax : variable_name.capitalize()

my_name1 = '''this method will return first letter Capital.
this method doesn't require any parameters.
o/p format is always a string.'''

print my_name1.capitalize()


#str.lower() : This method will return lower case converted string as output
#This method doesn't require any parameters.
#O/P format is always a string.  

#Syntax : variable_name.lower()

my_name2 = "BHARATH"

print my_name2.lower()


# 	str.upper() : This method will return upper case converted string as output.
#		      This method doesn't require any parameters.
#		      O/P format is always a string

#                     Syntax : variable_name.upper()

my_name1 = "bharath"
print my_name1.upper()


#       str.islower() : This method will return True if string is in lower case characters.
#        str.isupper() : This method will return True if string is in upper case characters.
#                        This method doesn't require any parameters
#                        O/P format is always a BOOLEAN OPERATOR.

#                      Syntax :  variable_name.islower()
#                                variable_name.isupper()

my_name1 = "bharath"
my_name2 = "BHARATH"
print my_name1.islower()
print my_name1.isupper()

print my_name2.islower()
print my_name2.isupper()


#       str.isalpha() : This method will return true only if the given string contains alphabetics  (a-z) and (A-Z).
#                      This method doesn't require any parameters
#                        O/P format is always a BOOLEAN OPERATOR.

#                                   Syntax : variable_name.isalpha()

my_name4 = "BhaRath"
print my_name4.isalpha()

#	str.isdigit() : This method will return true only if the given string contains numbers  (0-9).
#                       This method doen't require any parameters.
#                      O/p format is always a BOOLEAN OPERATOR.

#                     Syntax : variable_name.isdigit()

my_name5 = "123456789"
print my_name5.isdigit()



#	str.isalnum() : This method will return True only if the given string contains numbers  (0-9) or alpahbetics ( a-z A-Z) or Both.
#                       This method doen't require any parameters.
#                      O/p format is always a BOOLEAN OPERATOR.

#                     Syntax : variable_name.isalnum()

my_name5 = "Bharath123"
print my_name5.isdigit()



#	str.startswith() : This method will return True only if the given string starts with substring.
#                           substring can be a single characters or group of characters.
#                          This method  takes exactly one parameters.
#                          O/p format is always a BOOLEAN OPERATOR.

#                     Syntax : variable_name.startswith('substring')

my_name5 = "Bharath123"
print my_name5.startswith('Bh')
print my_name5.startswith('Bharat')


#	str.endswith() : This method will return True only if the given string ends with substring.
#                           substring can be a single characters or group of characters.
#                          This method  takes exactly one parameters.
#                          O/p format is always a BOOLEAN OPERATOR.

#                     Syntax : variable_name.endswith('substring')

my_name5 = "Bharath123"
print my_name5.startswith('3') 
print my_name5.startswith('123')


#	str.index() : This method will return index position of given substring .
#                     This method takes atleast one parameter and atmost two parameters.
#                      1st parameter represents substring  2nd parameter reperesents index position to start searching.
#                          O/p format is always an INTEGER.

#                     Syntax : variable_name.index('substring', default 0)
#                              variable_name.index('substing

#               NOTE : Index() will return error if substring not available in given string  { ex: substring not found}
#                       To avoid this devlopers introduced find method which will return -1 if substring not  found.
my_name5 = "Bharath123"
print my_name5.index('a') 
print my_name5.index('a', my_name5.index('a') + 1)


#str.find() : This method will return index position of given substring .
#                     This method takes atleast one parameter and atmost two parameters.
#                      1st parameter represents substring  2nd parameter reperesents index position to start searching.
#                          O/p format is always an INTEGER.

#                     Syntax : variable_name.find('substring', default 0)
#                              variable_name.find('substing', variable_name.find('substring')+1)

#               NOTE : find() will return error if substring not available in given string  { ex: substring not found}
#                       To avoid this devlopers introduced find method which will return -1 if substring not  found.
my_name5 = "Bharath123"
print my_name5.index('a') 
print my_name5.index('a', my_name5.index('a') + 1)


#str.replace() : This method will return the replaced string.
#                This method takes exactly two parameters, first parameter element to replace and  second element to place.
#                The output format is always a string.So we can perform all the string operations on replaced string operations.

#                      Syntax : variable_name.replace('element to replace', 'element to place')


s = "python"
print s.replace('o', '@')
print s.replace('o', '@').replace('p', 'P')


#str.split() : This method will return sliced strings which are splited by given substring.
#               O/P format is always  list of strings.
#              This method takes atmost one parameter and atleast zero parameter.
#               If no parameters given than python will split the string with "SPACE" by default.

#               Syntax: variable_name.split('element to split')

s = "Hello World"
print s.split()# Default parameter is space.
print s.split('l')#one parameter it can be a single character or group of characters.


#str.strip() :  This metod will return a string which is stripped by given substring
#               Stirp method will remove the give substring only from starting of the string and end of the string.
#               This method takes atmost one parameter i.e, element to strip with.
#               If no parameters given strip method takes space as default value.
#               The O/P format is always string
#               Syntax : variable_name.strip('element to strip with')

s = " python Grasp "
print s.strip('p')#It will return nothing because before p there is space.
print s.strip() # here default parameter is space

#str.format() : This method will return dynamic formatted string as output.
#               number of parameters required for format method = number of variables in dynamic string.
#                The o/p of format method is always a string.

#                Syntax : string_name.format(variable_name = "value", varible_name2 = "value", .....)


data  = ''' Dear {name} your journey details are bellow
from {station} to {desti} dated on {date} reporting time {time} '''
data.format(name = "bharath", station = "bangalore", desti =  "kadapa", time = "7:15PM", date = "12/08/2016")


#str.count(): This method will return number of occurances of given substring.
#             This method takes exactly one parameter i.e, substring.
#             The o/p format is always an integer.

#               syntax : variable_name.count('substring')



#str.splitlines(): This method will return list of lines in a given string(each line is an element in o/p list)
#                   NO parameters requred. O/P format is always a list.
#                           Syntax : variable_name.splitlines()



#str.encode() : This method will return encrypted data in particular format.
#               Python supports the below encryption formats in different versions.
#  base16, base32, base64
# utf-8, utf-16, utf-64
#                            This method takes exactly one parameter i.e., ecryption format.
#                  O/p format is always a string.
#               Syntax: variable_name.encode("encryption format")
                
s = "python"
b= s.encode("base64")


#str.decode() : This method will return encrypted data in particular format.
#               Python supports the below encryption formats in different versions.
#  base16, base32, base64
# utf-8, utf-16, utf-64
#                            This method takes exactly one parameter i.e., ecryption format.
#                  O/p format is always a string.
#               Syntax: variable_name.decode("encryption format")
                










 

