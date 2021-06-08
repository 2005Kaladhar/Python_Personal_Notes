'''
While importing and creating modules , it is to be noted that
when we create or own module and import it in other program, we are
intended to use its functions, variables, classes etc.

But it is also possible that we have written some code in that module
fuile to test the functions and when we import the file, those statements
are automatically executed and thus our program does not work properly.

For example -
1. Creating a file named my_mod.py
def func(string):
    print(f"The string '{string}'has {len(string)} no. of characters")

name = 'kaladhar'
func(name)

2. Creating another file named 'main.py'

import my_mod
country = 'India"
func(country)

Output -
The string 'kaladhar' has 8 no. of characters
The string 'India' has 8 no. of characters
--------------------------------------------------------------------
You will observe that the code written in the module file is aslo
automatically executed. Thus our attempt of successfully importing the
module is not satisfied.

To avoid this, we take the help of a special variable called
'__name__'
This variable is '__main__' when we are using the functions, classes etc
in the same file without importing it,
and when we import the file in some other program then this '__name__'
gives us the name of the python file in which we are importing our module.

Thus we can re-write the program in file 'my_mod.py' so that it will not
execute other statements while importing the file in 'main.py' file.

1. Re-Creating 'my_mod.py'

def func(string):
    print(f"The string '{string}'has {len(string)} no. of characters")

if __name__ == '__main__':
    name = 'kaladhar'
    func(name)

2. Re-creating another file named 'main.py'

import my_mod
country = 'India"
func(country)

Output -
The string 'India' has 8 no. of characters

#This time only the code in 'main.py' is executed not the code of the
module file.

Wohhoooo!! We learnt it .
Happy Coding!!...
--------------------------------------------------------

'''
