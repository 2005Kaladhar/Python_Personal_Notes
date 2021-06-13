'''
================Understanding types of methods.=====================

>> Types of methods
There are three types of methods.

1. Instance methods - That we generally make, the take the name of instance as their first argument

2. Class methods - Which take class name as the first arugment

3. Static methods - which are normal methods, they neither take class name nor instance name
they are used to perform functions which don't need the name of 
class or instance.


Note - While calling an instance method with the name of the instance,
then we don't need to specify the object as it automatically goes to
the class.

But if we want to run an instance method with the name of the class, then
in that case we need to specify the object like this - 

Employee - a class
kaladhar - an instance
print_details() - a method in Employee class

_____COde_________
Employee.print_details(kaladhar)
____________________


================= Understanding Class Methods ======================

As instance methods are used to perform some operation on the instance,
class methods are used to perform some operations on the class.

We define that a method is class method with the help of a decorator
'@classmethod'

class Employee:
    sick_leave = 10
    def __init__(self,naam,vetan,kaam):
        # Creating instance variables.
        self.name = naam
        self.salary = vetan
        self.role = kaam
        
    @classmethod
    def sick_changer(cls,new_leaves):
        cls.sick_leave = new_leaves
            
    def who_is_it(self):
        print(f"Name - {self.name}, Salary - {self.salary}"\
              f" Role - {self.role}")

kaladhar = Employee('kaladhar',456,'Student')

print("Before running the class method ",kaladhar.sick_leave)

#Changing sick_leaves from class name
Employee.sick_changer(50)   #We could have also done this with the class name.

# But the magic of class method is here.
kaladhar.sick_changer(50)   # This is the power of classmethod

print("After running the class method ",kaladhar.sick_leave)

-----------------------------------
Output-
Before running the class method  10
After running the class method  50
---------------------------------

Explanation - 
In the above class, we made a class method by using '@classmethod' decorator.
As an instance method takes the instance as the first argument, a class
method takes the class a the first argument.

-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------

======== Another way of changing class variables wih instance ========

.> We can access class of an instance with help of an attribute '.__class__'

________COde___________

class Employee:
    sick_leave = 10
    def __init__(self,naam,vetan,kaam):
        # Creating instance variables.
        self.name = naam
        self.salary = vetan
        self.role = kaam
        

    def sick_changer(self,new_leave):
        self.__class__.sick_leave = new_leave
    
    def who_is_it(self):
        print(f"Name - {self.name}, Salary - {self.salary}"\
              f" Role - {self.role}")

kaladhar = Employee('kaladhar',456,'Student')

print("Before running the class method ",kaladhar.sick_leave)

kaladhar.sick_changer(50)

print("After running the class method ",kaladhar.sick_leave)

-------------------------------
Ouput - 
Before running the class method  10
After running the class method  50
---------------------------------


============= Class method as an alternative constructor =============

.> Now we can use class method to make an alernatice constructor.
Task - Take only one string argument in class and make all the instance variables
from the constructor of the class.


class Employee:
    sick_leave = 10
    def __init__(self,naam,vetan,kaam):
        # Creating instance variables.
        self.name = naam
        self.salary = vetan
        self.role = kaam
    
    @classmethod
    def alter_construct(cls,constructor_string):
        return cls(*constructor_string.split(' '))

    def who_is_it(self):
        print(f"Name - {self.name}, Salary - {self.salary}"\
              f" Role - {self.role}")

kaladhar = Employee('kaladhar',456,'Student')

print("Before running the class method ",kaladhar.sick_leave)

kaladhar.sick_changer(50)

print("After running the class method ",kaladhar.sick_leave)

_______COde_______
class Employee:
    sick_leave = 10
    def __init__(self,naam,vetan,kaam):
        # Creating instance variables.
        self.name = naam
        self.salary = vetan
        self.role = kaam
    
    @classmethod
    def alter_construct(cls,constructor_string):
        # splitter = constructor_string.split(" ")
        # name = splitter[0]
        # salary = splitter[1]
        # role = splitter[2]
        # return cls(name,salary,role)
        
        #Or we can do it in a much better and cleaner way.
        return cls(*constructor_string.split(' '))

    def who_is_it(self):
        print(f"Name - {self.name}, Salary - {self.salary}"\
              f" Role - {self.role}")

kaladhar = Employee.alter_construct('kaladhar 456 Student')

print(kaladhar.who_is_it())

--------------------------------------------
Ouput - 
Name - kaladhar, Salary - 456 Role - Student
---------------------------------------------

Explanation - 

In the above code, we create a classmethod named 'alter_constructor'
which takes class name and a string in which all the values are separated
by space.

Inisde the classmethod, we are splitting the string with ' ' and getting 
a list of all the values that are to be given to class to make an object.

At the end we are returning the cls and passing all the arguments to it.
Conventional way is to first split it and then pass it one by one.

We can do this we the help of *args and directly passing all the values to
the class in single shot

-------------------------------------------------------------------------------
--------------------------------------------------------------------------------

                        Understanding @staticmethod
                        
                        
The third type of method in a class staticmethod. This mehtod neither takes class
nor an instance as its arguments, it acts like a normal function.

Q. Then what is the need of making it inside a class ?? We can make it outside
it .
Ans - Sometimes we want to make a function which should only be available to the
class, in that case we use staticmethod.


_______COde___________--

class Employee():
    
    @staticmethod
    def printer(to_print):
        print(f"This is a sample string .... {to_print}")
        

kaladhar = Employee()

Employee.printer("Ran By Class")
kaladhar.printer("Ran by instance")

--------------------------------------------------------------------
Ouput - 
---------------------------------------------------------------------
This is a sample string .... Run By Class
This is a sample string .... Run by instance






'''
class Employee:
    sick_leave = 10
    def __init__(self,naam,vetan,kaam):
        # Creating instance variables.
        self.name = naam
        self.salary = vetan
        self.role = kaam
    
    @classmethod
    def alter_construct(cls,constructor_string):
        # splitter = constructor_string.split(" ")
        # name = splitter[0]
        # salary = splitter[1]
        # role = splitter[2]
        # return cls(name,salary,role)
        return cls(*constructor_string.split(' '))

    def who_is_it(self):
        return (f"Name - {self.name}, Salary - {self.salary}"\
              f" Role - {self.role}")

kaladhar = Employee.alter_construct('kaladhar 456 Student')

print(kaladhar.who_is_it())





