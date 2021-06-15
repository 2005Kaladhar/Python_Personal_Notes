'''
     Understanding Public, Private and Protected Access Specifiers

While working with other programming languages like C++ or Java,
this concept is syntactically implemented by the complier.

In Python, it allows us to access all the variables outside the class
and internally there is nothing like it.

Public    - Can be accessed inside, outside and inside derived classes .
Protected - Can only be accessed inside the class, and in derived classes, not outside.
Private - Can only be accessed inside the class, not in derived classes and outside it


But as told earlier, in Python these things are not internally implemented.
We can access all these variables wherever we want but there are some conventions.

-------------------- Syntax of these variables ---------------------------------------
1. Public Variables - These are the normal variables that we have been defining for
a long time.

2. Protected Variables - These variables start with a single underscore '_'

3. Private Variables - These variables start with double underscore '__'
--------------------------------------------------------------------------------------


>> Protected Variables -

_________COde__________
class A:
    _my_protected = 45484

a = A()
print(a._my_protected)

----------------
output - 45484
---------------

>> Private Variables and Name Mangling

class A:
    __privateOne = 'This is a private string only class A can acces it'

a = A()
print(a.__privateOne)

-----------------------------------------------------
Output - NameError: name '__privateOne' is not defined
------------------------------------------------------

But as we know that the python does not impose any restriction on variables,
instead, it uses Name Mangling for private variables.

Here comes the role of Name Mangling in Python.

>> Name Mangling - It is process done by python to change to the name of
private variables so that programmer cannot use it outside the class accidently
or intentionally.

For this, it does not impose any restriction on the variable, rather it renames it
by prefixing '_CLassName' with the variable name.

For example - If we out private variable name is '__privateOne' in the class 'MyClass', then
Python interpreter will rename it as '_MyClass__private'

We can access it outside the class with the help of instance and class as follows -

__________COde_________

class A:
    __privateOne = 'This is a private string'

a = A()
# print(a.__privateOne)  # This will raise NameError
print(a._A__privateOne )  # This will give us the desired output

-----------------------------------
Output - This is a private string
----------------------------------

>> The same thing applies for instance variables.

_______COde_________
class A :
    def __init__(self):
        self.__privateOne = 'This is a private string'

a = A()
# print(a.__privateOne)  # This will raise NameError
print(a._A__privateOne  ) # This will give us the desired output

-----------------------------------
Output - This is a private string
-----------------------------------

'''
class A :
    def __init__(self):
        self.__privateOne = 'This is a private string'

a = A()
# print(a.__privateOne)  # This will raise NameError
print(a._A__privateOne  ) # This will give us the desired output
