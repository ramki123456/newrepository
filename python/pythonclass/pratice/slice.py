s="python"
print dir(s)

#dir: this method will return list of functions which  can perform on given variable.this method take exactly one parameter that var_name
#syntax: dir(var_name)
#-capitalize:- this method will return paragraph formatted string as output. this method does not req any no output formatt is always a string
#syntatx-string_name=capitalize()
#ex:s="python" s=s.capitalize()
#lowercase: this will return lowercase string as output. this method does not req any parameter 
#ex:s.lowercase()
#upper:-this method will return uppercase converted string as output. no parameter req. output format is always a string
#ex: s.upper()
#islower(): this method will return if the given string have only lowercase. no  parameter req output format always boolean
#ex:s.islower()
#isupper(): this will return true if the give string contains only uppercase. no parameter req. output formatt is always boolean
#ex: s.isupper()
#isalpha: this method will return true only if the given string contains alphabetis (a-z, A-Z) no parameter req the output format is always boolean
#syntax: string_name.isalpha() ex: s.isalpha()
#isdigit(): this method will returns only if given string contain digits(0-9). no parameter req. output format is always boolean
#ex: s.isdigit()
#isalnum: this method will return to only if the given string contains either alphabetis or no or both. no par req. output format is always a boolean operator
#string_name.isalnum()
#s="python123"
#isstartswith: this method will return to only if the given string is strats with substring. this method takes exactly one parameter that is substring. the output format is always a boolean
#string_name.isstartswith()
#ex: print s.startswith('py')
#endswith(): string_name.endswith(substring)
#this method will return to only if the given string endswith substring. this method takes exactly one parameter that is substring output format is always boolean.
#ex: s.endswith('py')
#s.endswith('on')
s1="hello world"
s1.index('o')
s1.index('o', s1.index('o')+1)