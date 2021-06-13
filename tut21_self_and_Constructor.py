'''
Undetstanding 'self' keyword and constructor '.__init__' in OOPS

> Functions created inside a class are called 'methods'

Creating a method of a class Employee-

----------------------------------------------------------
Note - Difference betweem parameter and argument.
. Parameter - things which need to be passed to a function.
. Arguments - things which are given to a function while calling it.
----------------------------------------------------------------

__________COde_____________________-

class Employee:
    def who_is_it(self):
        print(f"Name - {self.name}, Salary - {self.salary}"\
              f" Role - {self.role}")

kaladhar = Employee()

kaladhar.name = "kaladhar"
kaladhar.role = 'student'
kaladhar.salary = 786

kaladhar.who_is_it()

-----------------
Ouput - 
------------
Name - kaladhar, Salary - 786 Role - student

---------------------------------------
Explanation - In the above class Employee, we created a method named
------------
'who_is_it', in that method, the first parameter is 'self'.

As we know that we can instance methods on any instance, while 
running any method, it is the convention that the instance will
be given to the method as its first argument and to handle it 
we use 'self' keyword.

'self' should be the first parameter of every method of a class
except it is a static method or a class method which will be 
discussed later.


Q. What is the first parameter of a method ?
Ans - 'self' is the first parameter of a method.

Q. What is the first argument given to a method ??
Ans - The instance itself on which the method is applied
is the first argument given to the it.


------------------------------------------------------------------------
-------------------------------------------------------------------------
                    Understanding Constructor
                    
                    
In the previous exmaple of Employee class, we manually created
instance variables like 'name', 'salary', 'role' etc.

What if I need such variables 'name', 'salary', 'role' etc. for 
every instance of Employee class ??

Manually creating the same variables for every instance breaks the
rule of DRY .

If we want to do a specific task at the time of creation of an instance
of the class, we use constructors.

. Constructor is a special method which is automatically run by any
class while creating an instance(object).

>> Creating a constructor and re-writing the previous code

__________COde__________

class Employee:
    def __init__(self,naam,vetan,kaam):
        # Cerating instance variables
        self.name = naam
        self.salary = vetan
        self.role = kaam
    
    
    def who_is_it(self):
        print(f"Name - {self.name}, Salary - {self.salary}"\
              f" Role - {self.role}")

kaladhar = Employee('kaladhar',456,'Student')

kaladhar.who_is_it()

# Accessing instance method with the help of class 
Employee.who_is_it(kaladhar)

----------------------------
output - 
Name - kaladhar, Salary - 786 Role - student
------------------------------


Q. Where do the arguments given to a class go ?
Ans - All the arguments give to a class go to its constructor.


>> How to acces intance method with the name of a class ???
Ans - As we know that when we call an instance method with its name,
automatically the instance is given as the fist argument to the method and 
there we don't need to specify the instance.

But if we want to run an instance method with the help of a class, then
in that case we'll have to provide it the instance.




-----------------------------------------------------------------------





'''
class Employee:
    def __init__(self,naam,vetan,kaam):
        # Creating instance variables.
        self.name = naam
        self.salary = vetan
        self.role = kaam
    
    
    def who_is_it(self):
        print(f"Name - {self.name}, Salary - {self.salary}"\
              f" Role - {self.role}")

kaladhar = Employee('kaladhar',456,'Student')

kaladhar.who_is_it()

# Accessing instance method with the help of class 
Employee.who_is_it(kaladhar)
        
        






