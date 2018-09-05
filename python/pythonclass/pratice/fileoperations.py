'''file operations:- by using python programming language we can work on multiple file format like text, excel, word doc.
but by default we can work on text files without using extranal modules.
to work with text files python provides an inbuilt function named as open.
on a text file we can perform 3 major operations they are read, write and append.

open('filename', 'operation mode(read,write,append)')
fp = open('name.txt', 'r')
print fp
print dir(fp)

to work with read operation mode the file should exist.
open method takes atleast one parameter and atmost two parameter.
first parameter represent file name in string format. second parameter represents file operation mode.
open method represents file pointer method which contain approiate function to  be perform.
file_pointer = open('filename with path', 'operation mode').
in above syntax operation mode is the default parameter and the default mode is always read.

read - 'r'
write - 'w'
append - 'a'
read+ - 'rb+'
write+ - 'wb+'


to open a file in read operation mode use the second parameter as 'r'.
in read operation mode we can only access the data from given file.

fp = open('name.txt', 'r')
print fp.read()
print fp.read(5)
fp.seek(0)

this method is used to return in format of string. this method takes atmost one parameter that is index position.
if no parameters given then read method will return complete data.
whenever the read operations perform on a text file the file pointer will change its index position ahead.
to reset the file pointer position use seek method 

note: seek method takes index position as input and it will reset the pointer to given index position.

syntax: filepointer.read(index)

readline: this method will return first line of the file.
syntax: fp.readline(index)
ex:fp.readline(1)

readlines():- this method will return all the lines of the file in the format of list.
this method does not require parameters.
output format is always a list.

ex: fp.readlines()

write: use operation mode as 'w' to work with files.
when we work on file operation python create new file and replace it which already exist.
fp = open('name.txt', 'w')
python supports two types method in write operation mode they are write and writelines.

fp.write('hello')

writelines:- this method is used to insert a string into file this string may contain single or multiline
this method takes exactly a list.'''

syntax: fp.write([group elements])
fp = open('name.txt', 'w')
fp.writelines(['hi', 'hello', 'world'])
print fp

writelines:this method is used to insert multiple strings.
this method takes exactly one parameter
writelines method will take datastructure as input but the datastructure should contain strings.

append: 
to work with append operation mode the file should exist
append method will also comes with write and writeline methods which will works as write operation methods.

fp = open('data text', 'a')
fp.write('hi'
	'hello')
fp.writelines()

rb+ = read + write + append
wb+ = write + read + append
