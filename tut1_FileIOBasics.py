""" Different modes of file in python

1. 'r' - Read (Default)
2. 'w' - Write
3. 't' - Text (Default)
4. 'b' - Binary 
5. 'x' - Creates a file if doesn't exist otherwise raises FileExistsError
6. '+' - Reading and writing
7. 'a' - Append, add items at the end of a file.


"""
# Reading from a text file 
'''
1. Iterating the file
2. Using read() method - returns a string (a kind of multi line string is returned)
3. Using readline() method
4. Using readlines() method

'''
# Using read() method
# file = open("kaladhargopal.txt",'r',encoding='utf-8')
# content = file.read()
# print(content)
#__________--------______-------______------______------_______------______------____--------

# Iterating over the file
# file = open('kaladhargopal.txt','r',encoding='utf-8')
# for line in file :
#     # print(line)   # It will put a \n character and there will be double space between lines
#     print(line,end='')
#___________---------------______---------------------______________-------------________________-----------

#Using realine() method
# file = open("kaladhargopal.txt",'r',encoding='utf-8')
# content = file.readline() #Gets a single line
# print(content)
# '''On Running it again, it will print the next line of the file/  '''
# content = file.readline() #Gets a single line
# print(content) #prints the second line of the file because the pointer has been thrown to next line.
# _______--____--------___------_____----_____-----____-----_____-----____-----____----_____----_____--___---


#Using readlines() method
#used when we want to store all the lines in list
# file = open('kaladhargopal.txt','r')
# content_list = file.readlines()
# print(content_list)
# print(f"the file is of type : {type(content_list)}") 
 #____-----_____-----______----_____-----_____-----_____-----_____----_____-----_____-----_____----------__--
 
 
#When we write a number inside readline() and read() method the it reads the given number of characters from the file
 
# file = open('kaladhargopal.txt','r',encoding='utf-8')
# content = file.read(4) # or file.readline(4) both will have the same result
# print(content)
#_______--_________---_______---______----_____----______---_____----_____---_____----______---____----__

#WHen we write a number except 0 inside realines() method it always returns the second line, if 0 then
#it reads the whole file and works normally as it is expected to do.
# file = open('kaladhargopal.txt','r',encoding='utf-8')
# content = file.readlines(0)  # IT will give the same result as file.readlines()
# content_2 = file.readlines(1) # Returns the second line 
# print(content)
# print(content_2) # It will print empty list because the file has been read by the previous line.
 
 