'''
Recap -

Name Mangling - It is the process in which name of private variable is prefixed
by _classname


1. Bulit in polymorphic functions - min(), max(), len(), str()
2. User defined polymorphic functions / Duck Typing.
3. Polymorphism in inheritance
4. Method overriding
5. Method overloading

---------------------------------------------------------------------------------
--------------------------------------------------------------------------------

                Dunder Methods and Operator OVerloading

Methods which start and end with '__'(double underscore) are called 
Dunder Methods or Magic Methods.

Dunder methods cannot be called directly, they are internally called 
by the class on certain actions.


>> Operator Overloading - Overloading the 'operator dunder methods' of 
class is called operator overloading.

This is called 'Overloading' not overriding because they we not defined
anywhere before nor they are inherited by a class, thus this process is 
called Overloading not Overriding.

These 'Operator Dunder Methods' are not defined anywhere, therefore 
when we define them, it is called 'Overloading' while some dunder
methods are internally defined and used by the class like 
'__new__' dunder method which is called even before the constructor.


-------------------------------------------------------------------------
-------------------------------------------------------------------------
Q. Which method is called first method by any class ?
Ans - __new__ is the first method called by any class even before the
constructor '__init__'.
-------------------------------------------------------------------------
-------------------------------------------------------------------------


        Understanding Some Important Dunder Methods 

__str__()
__repr__()
__new__()

__add__()
__setattr__()
__getattr__()

__del__()
__hash__()


The most common dunder method that almost all the classes have is 
the cosntructor "__init__".


''' 
class Employee(object):
    
    leaves = 45
    
    def __init__(self, data):
        super().__setattr__('data', dict())
        self.data = data
    
    
    def __getattr__(self, name):
        print("wohoooo")
        if name in self.data:
            return self.data[name]
        else:
            return 0
    

    
    def __setattr__(self, key, value):
        print(key,value)
        if key in self.data:
            self.data[key] = value
        else:
            super().__setattr__(key, value)
            
    
 
 
emp = Employee({'age': 23, 'name': 'John'})
gopa = Employee({'age': 23, 'name': 'John'})
emp.role = 'Kaladhar'
        
