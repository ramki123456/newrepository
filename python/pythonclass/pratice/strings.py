#replace:- this method will return the replaced string. this method takes exactly two parameters
#(element to replace, element to place). the output format is always a string so we can perform all string operations.
#strin_name.replace(element to replace, element to place)
#s="python"
#print s.replace('o', '@')='pyth@n'
#print s.replace('y', '!')='p!th@n'

#split:- this method will return slice which are splitted. output format is always list of strings. this method takes atmost one parameter at least zero par. if no parameters given then python will split with space.
#string_name.split(element to split)
#s="python"
#s.split("")
#print s.split("l")

#strip:- this method will return a string which is stripped by given substring. strip method will remove the given substring only from left and right. this method takes atmost one parameter that is element to strip. if no parameter given strip method takes space as default value. the output format is always string.
#string_name.strip("at most one parameter")
#s="python grosp"
#s.strip("p")
#s.strip("py")

#format:- this method will return dynamic formatted string as output. no of parameters req for format method is equal to member var in dynamic string. the output of formatt method is always a string. 
data='''dear {0}
your ticket been booked from {1} to {2} on {3} at {4}
thank u and visit again.'''

print data.format("ram", "ban", "bng", "12/8/2016")
#syntax: string_name.format(variable_name="value", variable_name2="value")
data='''dear {0}
your ticket been booked from {1} to {2} on {3} at {4}
thank u and visit again.'''
print data.format(name="ram", source="ban")
#in 2.7.6 format method will work with any parameter in 2.7.11 we should pass req no of parameters.

#count:- this method will return no of occurance of given substring. this method takes exactly one parameter that is substring the output format is always an integer.
#syntax: string_name.count("substring")
s="python programming"
s.count('o')
#splitlines: this method will return list of lines in given string each line is an element in  list. no par req output format is always a list 
#string_name.splitline()

#encode:-

