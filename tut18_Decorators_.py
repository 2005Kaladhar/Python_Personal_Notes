'''
Understanding decorators in python.
------------------------------------

Before understanding decorators we need to know that in python
functions are first class objects.

Properties of first class objects 
------------------------------------

1.They can be stored in a variable.

2.They can be given as an argument to another function. - like in map(), filter() etc.

3.Function can be returned by a function.

4. We can store functions in data-structures such as lists, tuples etc. - Just like the advaced usgae that we saw in the previous tutorial.


== Storing a functino in a variable
my_printer = print
my_printer("Printing from my own print function")

Output - 
Printing from my own print function



----------------------------------------------------------------------------

Decorators  - These are the functions which are used to modify a given
without permanently changing the code of the function.

In Lyaman's words - Decorator is a wrapper function which wraps and 
modify a given function.


For exmaple  - 
-----------------
def modifier(func):
    def inner():
        print("Printing before executing the function.")
        func()
        print("Function executed....")
    return inner
    
def calculator():
    print(f"Calculated Value is -> {8+5}")


calculator  = modifier(calculator)

calculator()

---------------------
Output - 
-----------------------

Printing before executing the function.
Calculated Value is -> 13
Function executed....

Explanation - In the above example the wrapper function is 'modifier'
and the function which is being modified is 'calculator'.

The modifier function prints something before and after the execution
of the given function.


==> Giving arguments to a function and then modifying using 
decorator.

Taking the previous example - 

def modifier(func):
    def inner(x, y):
        print("Printing before executing the function.")
        func(x,y)
        print("Function executed....")
    return inner
    
def calculator(x,y):
    print(f"Calculated Value is -> {x+y}")


calculator  = modifier(calculator)

calculator(5,8)

---------------------
Output - 
-----------
Printing before executing the function.
Calculated Value is -> 13
Function executed....


Explanation - In the above program, the decorator 'modify()' returns a function
'inner', to modify a function which takes some arguments, we need to make the 'inner'
take the same numeber of arguments as the function to be modified takes and while 
calling the function inside 'inner' we need to pass the arguments to the function.
__________________
------------------
==> Behind the scene  - In the above code, when we are writing
------
calculator = modifier(calculator)

> 'modifier(calculator)' this returns the 'inner' function and now 
'calculator' function is pointing to 'inner' function.

> when 'calculator(5,8)' is called, then it is actually calling 'inner(5,8)' and 
inside 'inner' function, it prints something, and then it calls the function
'func' and now this 'func' is the 'calculator' function which we had already 
specified before while wiriting 'calculator = modifier(calculator)'.

--------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------
                            Using ' @ ' to make decorators
                            -------------------------------
Taking the previous example - 

def modifier(func):
    def inner(x, y):
        print("Printing before executing the function.")
        func(x,y)
        print("Function executed....")
    return inner
    
@modifier
def calculator(x,y):
    print(f"Calculated Value is -> {x+y}")


calculator(5,8)                   

---------------------
Output - 
-----------
Printing before executing the function.
Calculated Value is -> 13
Function executed....


Explanation - In the above program we can specify the decorator while 
creating a function by writing the name of the decorator function above 
the given function to be modified by starting with '@' symbol.

---------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------
                    Making a decorator to calculate execution time of a function
                    ------------------------------------------------------------
                    
Points -  We can get the name of a function, say 'func' by writing 
            func.__name__


import time

def time_cal(func):
    def inner(x, y):
        t1 = time.time()
        func(x,y)
        t2 = time.time()
        print(f"Function \"{func.__name__}\" executed in {t2 -t1:.8f}seconds.")
    return inner
    
@time_cal
def calculator(x,y):
    print("Printing before calculation.")
    print(f"Calculated Value is -> {x+y}")
    print("Value has been calculated.")


calculator(5,8)

--------------
Output -
-----------

Printing before calculation.
Calculated Value is -> 13
Value has been calculated.
Function "calculator" executed in 0.00006700seconds. 




 =============Making a general decorator====================
 
 Q. What if a decorator is to be made which can run on any
 function?? And How to get the reutrned value of the function ??
 
 1. Making a general decorator.
 A general decorator can modify any function taking any numeber of 
 positional and keyworded arguments.
 
 
from time import time, asctime, localtime
 
def time_cal(func):
    def inside(*args, **kwargs):
        print("Starting time calculator")
        t1 = time()
        returned_val = func(*args, **kwargs)
        t2 = time()
        print(f"Function executed in {t2-t1:.8f} seconds")
        return returned_val
    
    return inside

@time_cal
def get_date_time():
    today = asctime(localtime())
    return str(today)

date_  = get_date_time()

print(date_)
---------------
Output - 
---------------
Starting time calculator
Function executed in 0.00005531 seconds
Fri Jun 11 13:38:58 2021

--------------
Explanation - In the above code, inside the decorator function
and in the wrapper function 'inside()' I gave *args and **kwargs 
as the arguments and aslo passed *args and **kwargs while calling the
main function 'func'. This makes the decorator a general decorator, it 
will give all the positional and keyworded arguments to the function.

 
=================================== Chaining Decorators ===============

>> We can chain decorators as follows - 
_____________COde_____________

def add_1(func):
    def inside():
        val = func()
        print("Adding 1 ")
        return val +1 
        
    return inside

def add_2(func):
    def inside():
        x = func()
        print("Adding 2 ")
        return x +2 
    return inside

@add_2   
@add_1
def num_generator():
    return 5
    
value = num_generator()
print(value)
-------------------
Output - 
-------------------
Adding 1 
Adding 2 
8

 
 
Explanation - In the above function, we are modifying function 'num_generator'
with 'add_1' and "add_2" decorators. 

While chaining decorators, it should be noted that the decorator specified at
the end will be executed first. Here, 'add_1' is specified at the end, hence
it is executing first and "Adding 1" is printed first and then "Adding 2" is 
printed.

The above chained decorators can be written as : -

num_generator = add_1(add_2(num_generator))


. First, add_1 is executed which called add_2 and this called num_generator
which returned '5', then add_1 added '1' to 5 and then add_2 added '2' to '5+1'
and finally returned the result '5+1+2' = '8'.


Again, if the function to be modified takes some arguments, then all the 'inside'
functions of the decorators must take the same number of arguments as the 
function to be modified takes. 

So, if num_generator takes some arguments then we'll have to write the code as -

___________Code___________
def add_1(func):
   
    #def inside(a):                # It should accept the same number of arguments as 'num_generator' takes
    def inside(*args,**kwargs):     #Or we can do this to accept all the arguments and become tension free
        val = func(*args,**kwargs)  # Giving the accepted argument to the function
        print("Adding 1 ")
        return val +1 
        
    return inside

def add_2(func):
    
    #def inside(a):                 # It should accept the same number of arguments as 'num_generator' takes
    def inside(*args,**kwargs):     #Or we can do this to accept all the arguments and become tension free
        val = func(*args,**kwargs)  # Giving the accepted argument to the function
        print("Adding 2 ")
        return x +2 
    return inside

@add_2   
@add_1
def num_generator(num):
    return num
    
value = num_generator(5)
print(value)

Note - In the above code, to get rid of the tension of counting arguments of the function and 
specifying them in all the decorators, we can make them general decorators by giving *args and
**kwargs in their 'inside' function.




'''

'=================== Example Code For Practice and Revision =================='
from time import time 


def add_2(func):
    def inside(*args, **kwargs):
        a = func(*args, **kwargs)
        print("Adding 2")
        return a+2
    return inside

def add_1(func):
    def inside(*args, **kwargs):
        a = func(*args, **kwargs)
        print("Adding 1 ")
        return a+1
    return inside

def time_cal(func):
    def inside(*args, **kwargs):
        print("Starting time Calculator...")
        t1 = time()
        a = func(*args, **kwargs)
        t2 = time()
        print(f"All the functions are executed in {t2 -t1:.8f} seconds")
        return a 
    return inside

@time_cal
@add_2
@add_1
def number_generator(num=5):
    return num

user_inp = int(input("Enter your favourite number : "))  # For Example 5
value = number_generator(user_inp)

print(value)

'''
------------
Output - 
-----------
Enter your favourite number : 5
Starting time Calculator...
Adding 1 
Adding 2
All the functions are executed in 0.00002098 seconds
8

-------------------------------------
Note - In the above program, we specified time_cal decorator first because we want it 
to run at the end so that we can calculated the execution time all the events.


First time_cal will be called, which will call its 'inside' function and it will call
add_2 which will return its 'inside' function and finally it will called num_generator 
function which will return 5. 

.At this point all the decorators are not executed 
completely and waiting for the underlying functions to complete their execution,

.once num_generator returns 5, then add_1 will continue execution and add 1 to it
and return the result 5+2

.then add_2 function will continue its execution, add 2 to it and return 5+1+2
and finally the time_call will continue and 't2' variable will get the ticks 
and at the end the calculated time is printed and the final result 5+1+2 = 8 is returned.


'''

