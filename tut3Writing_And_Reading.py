'''
--------------------------------------------------------------------
Creating a file if it doesnt exist in writing and reading mode,
writing and reading from a file at the same time.

Mode for file - 'w+'

file = open("kaladhargopal.txt",mode='w+',encoding='utf-8')
#Writing in the file
file.write("Hello world this is kaladhargopal\nthis is second line.")
#NOte - Now the cursor is at the end of the last line.
#To read it, we need to take the cursor to the beginning. Therefore,
print(f"Cursor position has changed to {file.tell()}")
file.seek(0)
content = file.read()
print(f"\nContent of the file is as follows :\n{'':->20}\n{content}")

Output :
Cursor position has changed to 54

Content of the file is as follows :
--------------------
Hello world this is kaladhargopal
this is second line.

'''





