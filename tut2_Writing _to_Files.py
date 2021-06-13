"""
Reading an writing in a file at the same time
to read and write in a file at the same time, we need to opent the file in 
'+' mode.

"""
file = open("kaladhargopal.txt",'r+')
content  = file.read()
print(content )
file.write("\nTo yrr bas itna he tha isme...")
file.close()

'''
Note :- When we open a file in 'x' mode then it will create the file if it does
not exist otherwise gives FileExistsError.

But if we try to open a file in 'w' mode then it will create the file if it 
does not exist and if it exists then it will delete all the data in the file 
and it will write the data that is given in the program.

Also 'r+' mode will also throw FileNotFoundError when file does not exist.

Conclusion - 'w' mode can act like 'x' mode but 'x' mode cannot act like 'w' mode.
'''




