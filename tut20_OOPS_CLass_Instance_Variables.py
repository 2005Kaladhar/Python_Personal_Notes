'''
Understanding Instance Variables and Class Variables
----------------------------------------------------------------------------

> Instance variables - These are the variables which are just limited to instance, it means
that other instances and even the class cannot access instance variables of an object.
They can only be changed by the instance itself.

> Class Variables - These variables are available to all the instances of the class, but, it can
only be changed by the class itself.

___________COde_______________

class Employee():
    hrs_to_work = 8


kaladhar = Employee()     # Instance 1
gopal = Employee()        # Instance 2

kaladhar.name = "Kaladhar"   # Instance variable for 'kaladhar'
gopal.name = "Gopal"      # Instance variable for 'gopal'

kaladhar.salary = 456
gopal.salary = 786

print(kaladhar.salary)

#Example to show that class variables are for all the instances.
print(kaladhar.hrs_to_work)  
print(gopal.hrs_to_work)

Employee.hrs_to_work = 78   #Changing Class Variable

print(gopal.hrs_to_work)        # Accessing Class Variable with instance
# print(Employee.hrs_to_work)   # We can also acces class variable with class name. 
 
-------------
Output - 
------------
456
8
8
78
------------------------

Note - While defining a class name, it is optional to write parenthesis '()' after the
class name, we use parenthesis to define the parent classes (In Inheritance).

For a class which is not a child class i.e when not using inheritance, it is optional to 
write '()' after class name. We need it when inheriting from other classes (No need to worry now.)

Explanation - IN the above code, kaladhar and gopal are two instances 
of Employee class.
They have some instance variables like name, salary, role etc.

>> Employee class has a class variable 'hrs_to_work' which can be accessed by all the instances.
If we try to change a class variable with the help of an instance, then it will create another
instance variable of that name.

>> To change class variable, we need the class itself, in the above
code "Employee.hrs_to_work" can be used to change the class variable.







'''

class Employee:
    hrs_to_work = 8


kaladhar = Employee()     # Instance 1
gopal = Employee()        # Instance 2

kaladhar.name = "Harry"   # Instance variable for 'kaladhar'
gopal.name = "Rohan"      # Instance variable for 'gopal'

kaladhar.salary = 456
gopal.salary = 786

print(kaladhar.salary)

#Example to show that class variables are for all the instances.
print(kaladhar.hrs_to_work)  
print(gopal.hrs_to_work)




