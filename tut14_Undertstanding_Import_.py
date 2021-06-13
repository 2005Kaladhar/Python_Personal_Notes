'''
We can install any module or a library in our machine with the help of
Python Package Manager named 'pip'

TO use a module in our program, we can import it with the help of 'import'
keyword.

---------Undestanding How Import works--------------------
Whenever we import a module or a library in our program, our python
interpreter first searches it in our current working directory and then followed
by some other directories.

Therefore, we should be very careful while naming our program files, we must
not name out program file with the name of any module or library.

==> Getting the paths of the directories from where pyton interpreter imports
modules.

import sys
print(sys.path)

it will give us list of all the paths form where it imports.

------Uderstanding Methods of importing--------------------
1. The very first method of importing something in our program is to import the
whole module by writing,

import <module_name>
for example  - import time

-->Demerit - It is not a good practice when working with applications and huge
programs, as our python interpreter will import the whole module and those
unnecessary things which we do not need in our program thus making it slow.
----------------------------------------------------------
2. Selective import
We can selectively import certain class ,function etc from a module

syntax - from module_name import name_of_required_thing

for example - if I need time function of time module not the entire module,then
I can selectively import time function as follows -

from time import time
print(time())

Note - When we selectively import something in our program we should not
specify the name of the module, just directyl use it otherwise it will raise
ERROR (AttributeError).

from time import time
print(time.time()) X - Error
print(time()) - Yes


-----What is good for us ??----------
For beginners, it is always best to import the entire module to use its
functions and methods. WHy??

Suppose we are selectively importing a function two modules and the name of
that function is 'func' in both the modules, and if we use it in our program
then interpreter will not be able to resolve from which file it should bring
'func' function.

-------Creating our own module-----------
As we know that, python interpreter first searches for the imported file in
the current working directory, we can make import a file from our directory.

This method can be used to write some important self made functions or classes
in a particular file , copy it to current working directory and then use it.

'''
