############## File operations #######################
# File operations 
        # By using python programming language we can work on multiple file formats like
           # text file, excel file, pdf file and csv file etc....
        # But by default we can work on txt files without using external modules.
        # To work with txt file python provides an inbuilt function named as open().
        # On a text file  we can perform three major operations they are 
            # read['r'], write['w'] and append['a']. other 'rb+' 'wb+'

#'close', 'closed', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'mode', 'name', 'newlines', 'next', 'read', 'readinto', 'readline', 'readlines', 'seek', 'softspace', 'tell', 'truncate', 'write', 'writelines', 'xreadlines'


# Read:-
            # To work with read operation mode the file should exits.
            # open method takes  atleast one parameter and atmost two paramters.
                       # First parameter represents file name in string format,
                       # second parameter repersents file operation mode.
            #open() return file poointer object which contains apropriate funcions to be performed.
  
			 #syntax : file_pointer = open('file path', 'r')
        # In above syntax operation mode is the default parameter and the default mode is always 'read'.
        # To open a file in read operation mode uses second paramter as 'r'
        # In operation mode we can only access the data from given file.



fp = open('/home/bharath/Desktop/pythonclass/data.txt', 'r')

    #.read() : This method is used to return the complete file return in the format of string.
        #  This method takes atmost one parameter i.e., index postion.
        #  If no parameter is given than read method will return complete file data as it's 
        # where read operations perform on a text file the file pointer will change it's index position.
        # To reset the file pointer position use """ seek() method ""

                # syntax : file_op.read()

    #.readline(): This method will return the first line of the file.
             #This method takes atmost one parameter i.e., index postion.
             #  If no parameter is given than read method will return complete file data as it's 
            # where read operations perform on a text file the file pointer will change it's index position.

                    #sytax : file_op.readline()

    #.readlines():  This method will return all the lines of the file in the form of lists.
              # This method doesn't require any parameters.
              # o/p format is always list.

                   # syntax : file_op.readlines)


#.seek() method takes index position as input and it will reset the pointer to given index position.

print fp.seek(0)
#print fp.read()
#print fp.readline()
name = fp.readlines()
print name

print type(name)


# Write :-
         # use operation mode as 'w' to work with write operation.
         # When we open a file in write operation mode python will create an empty document and replaces the orginal file if the file allready exits.
         # python supports two types of methods in write operation.

                           #syntax : file_pointer = open('file path', 'w')

 
      # write() : This method is used to insert a string  into the file.
                # The string may contain single line or multilnes.
                # This method takes exactly one parameter.o/p will not return anything.
                 
                         # syntax : fp_name.write()

     # writelines(): This method is used to insert multiple strings.
                   # This method takes exactly one parameter i.e, datastructure. should contain only strings 
                    
                         # syntax : fp.name.writeline([' ' , ' ' , ' ' , ' ' ])



fp_name = open('/home/bharath/Desktop/pythonclass/dat.txt', 'w')
print fp_name.writelines(['Hi\n', 'hello\n', 'world\n', 'today \n', 'I am\n', 'learning python\n'])




# Append :- 
            # To open a file in append operation mode use 'a' as second parameter in open method.
            # To work with append operation mode the file should exist.
            # Append method will also comes with .write() and .writelines() methods which will work as wirte operation mode methods.


               #syntax : file_pointer = open('file path', 'w')

fp_name = open('/home/bharath/Desktop/pythonclass/dat.txt', 'a')
fp_name.write("myworld exist with me")
print fp_name.read()


