'''
Args and Kwargs deep dive in Python.

Q. Need of *args and **kwargs in a function.
Ans - Sometimes we may need to pass multiple arguments to a function so in that
case we will have to define multiple arguments for the function.
So, this is not a convenient method to do it, in that case we take the help
of *args argument.

Similary, when we need to give multiple keyword arguments (like a dictionary),
then we take the use of **kwargs argument.

------------------------------------------------------------------------
Understanding different aspects of *args and **kwargs.

Note - In any function, defining args and kwargs is completely optional,
even if a function has these arguments and we don't pass anything while
calling them, it will not raise any error.

------------------------------------------------------------------------
==> Undestanding *args (args is a convention, we give it any name followed by *)

def func(*args):
    print("Following are the students of our University :")
    for items in args:
        print(items)

func('kaladhar','gopal','mohan','rohan','vijay')

In the above example, we can give multiple arguments to the function.
And even if we don't give any argument, the function will not throw any error.

Another way of giving multiple arguments to the function.

def func(*args):
    print("Following are the students of our University :")
    for items in args:
        print(items)

arguments = ['kaladhar','gopal','mohan','rohan','vijay']

func(arguments)     # VVIMp
func(*arguments)    # VVimp

understanding difference between the above two callings
---
arguments = ['kaladhar','gopal','mohan','rohan','vijay']

func(arguments)     # VVIMp
In the above method, only one argument will be given to the function and that will be a list 'argument'

func(*arguments)    # VVimp
In the above example, all the elements of the list 'argument' will be parsed as arguments to the function.
It means that we use this method to pass the all the elements of a list as multiple arguments to a function.

Note - Again it is to be noted that if we don't give any argument to a function having *args and **kwargs
the function will not raise any error.

--------------------------------------------------------------------------------------------------
=> Understanding **kwargs (kwargs is a convention, we give it any name followed by **)

When we need to parse multiple keyworded argument to a function, we take the help of **kwargs

def func(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
func(name="kaladhar gopal",role='student',school='KV')

------------------------
==> Understanding difference between these two methods of parsing arguments to a function taking kwargs

dic = {'name':"kaladhar gopal",'role':'student','school':'KV'}

func(dic) - [ERROR] This will throw error as the function only takes keyworded arguments
The above method will work fine if there is *args, but there will ony one argument containing the dictionary

func(**dic) - This will parse all the key:value pairs as keyworded arguments to the function.

-------------------------------------------------------------------------------------------
Q. Can we parse a normal argument, **args and **kwargs at a same time to a function ??
Ans - Yes! we can, but we need to take care of the sequence in which these are accepted by a function.

function_name(normal_arg1,normal_arg2,**args,**kwargs)

Note - We cannot give **args and **kwargs externally as keyword arguments to a function as they are recognised as
positional arguments.
-------------------------------------
def func(normal,normal2,*args,**kwargs):
    print(f"Normal Arguments are : 1. {normal}\n2.{normal2}")
    print("**args are as follows - ")
    for i in args:
        print(i)
    print("\n\n**kwargs are as follows:-")
    for i,j in kwargs.items():
        print(f"{i}:{j}")
    print("Function ended...")

var = 'Normal argument 1 '
var2 = 'Normal argument 2 '
func(var,var2,'extra argument1','extra argument 2 ',name='kaladhar gopal',school="KV",role='Student')

Note - If we don't parse any arguments for *args and **kwargs, the function will not raise any error.
But if we don't parse any argument for (normal, normal1) arguments, then the function will raise TypeError
as we haven't parsed any argument for the required fields in the function.



'''
