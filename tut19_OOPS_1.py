'''
Introduction to OOPS - Object Oriented Programming System/Structure.
-----------------------------------------------------------------

Python is a multi-paradigm programming language - it means that 
python supports different styles of programming.
We may have - Functional Programming and Object Oriented Programming.

>> OOPS uses - DRY concept - (Don't Repeat Yourself).


Q. What is a class ??
---------------------
Ans - A class is just like a template from which we can create multiple
objects. In other words we can say that a class is collection of 
similar things which have similar functionality.

Suppose we want to write a letter, then we'll simplt write it in a
paper, but, what if we want to write 1000 letters for students ?
In that case we'll not write each letter from beginning, we can create 
a template and just replace some values like name, place, subject etc.

In that situation we used the concept of DRY, we did not repeat the same 
task of writing the same thing for each student.

Q. Then what is an object ??
------------------------------
Ans - Taking the previous example, the letter we create using the template 
of the letter will be called an object or instance of that class.
So, whatever we create from a class is called its object.


============= Creating a Class ===============

Creating a class is similar to create a function. Just like 
we create a function using def keyword, we create a class
using 'class' keyword.

syntax - 

class Class_name:
    pass
    
Note - It should be noted that the name of class is started with a capital 
letter. Interpreter will not raise any error if we don't follow it, but it
is a good practice to create class name starting with capital letter.

Creating an Employee class

class Employee:
    pass
    
emp1 = Employee()
emp2 = Employee()

#Further we can create instance variables 

emp1.name = 'kaladhar'
emp1.role = 'student'
emp1.height = '5ft 11inch'

# We can print instance variables like this

print(emp1.name)
print(emp1.role)
print(emp1.height)
 
----------
Output - 
----------
kaladhar
student
5ft 11inch



    
Note - Instance variables are those variable which can only be accessed 
by the particular instace. It cannot be accessed by other objects of the 
class.
    
It is to be noted that emp1 and emp2 are two different objects.
if we print(emp1 is emp2), it will print False.

-------------------------------------------------------------------------

.Attributes of a class - The Data of the Class --> Variables
.Methods of a class - fucntions in a class is called a Method
.Beahviour is determined by  ---> Functions (methods)
.Object of a class is called -->  an Instance of the class





'''




