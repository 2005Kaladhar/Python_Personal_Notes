'''
>> Pillars of Object Oriented Programming.
1. Abstraction
2. Encapsulation
3. Poylmorphism
4. Inheritance

The third pillar of OOPS is Polymorphism.
Polymorphism means ability to take different forms.

An object can take different forms as follows -
1. a = 56
Here 'a' is an integer literal

2.a = '56'
Here 'a' is a string literal.

In the above example we can see that 56 can take the form of
an integer as well as the form of string. This property is called
Polymorphism.

===================================================================
===================================================================

=== === === === Polymorphism in Object Oriented Programming. === === === ===

>>> 1. Polymorphic functions.

These are the functions which can take different types of
objects as their arguments. like - len(), type(), max(), min() etc.

for example -

a = [1,2,3,4,5]
b = (1,2,3,4,5)
c = 'kaladhar gopal'

print(len(a))
print(len(b))

print(min(a))
print(min(b))
print(min(c))

print(max(a))
print(max(b))
print(max(c))
-----------------------------------------------------------------

>> We can observe that we are running min(), max(), len() functions for
list, tuple and string type objects, these are the examples of
'Inbuilt-Polymorphic' functions.

>> Similarly we can create own polymorphic functions.



>>> 2. User defined Polymorphic Functions / Duck Typing .
Duck Typing - It doesn't matter which type of object it is, it should
have that behaviour (that method or attribute).

___________COde____________________
class A:
    def printer(self):
        print("Calling printer from class A")

class B:
    def printer(self):
        print("Calling printer from class B")

def func(obj):
    obj.printer()

a = A()
b = B()

for object in (A,B):
    func(object)

------------------------------------------------------------
>> In the above example, our user defined function 'func' is a
polymorphic function as it can take object of different types
here (from class A and class B) and can perform task on it.
>> Here we are assuming that both the classes A and B have
instance method 'printer'


>>> 3. Polymorphism in Inheritance

In inheritance we have the concept of "Method Overriding" this
is the implementation of Polymorphism in inheritance.

For this, there must be atleast two classes and there must
be inheritance.

If we define a method inside the parent class, then, while
inheriting, the child class will also get that method, but
if we want to change the method with the same name, then
we can define another method with the same name in child
class and this is called "Method Overriding"

________COde________

class A:
    def printer(self):
        print("Hello I am from class A")

class B(A):
    def printer(self):
        print("Hello I am from class B")

a = A()
b = B()

a.printer()
b.printer()

Output -
Hello I am from class A
Hello I am from class B
-----------------------------------------------------------------------
Explanation - In the above example we derived class B from class A
and with inheritance, method printer() also got inherited in class B.

Inside class B we override the method by creating another method
of same name, that's why while running b.printer() we got that
statement which we had written in the printer() method of class B.


>>> 4. Method OVerloading
In method overloading we create functions with same name but with different
functionalities, this is supported in languages like Java and C++ but Python
does not support Method Overloading. We can try to do this but we will able to
access only the latest defined function and the previous function will be inaccessible
for us.

_____Code_____

def prod(a,b):
    print(a*b)

def prod(a,b,c):
    print(a*b*c)

prod(1,2,3)
-----------------------------------------------
Output - 7
------------------------------------------------
We can only access the latest defined function. :(


'''
