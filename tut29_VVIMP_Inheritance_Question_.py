class A :
    classvar1 = "CLass variable in class A"
    def __init__(self):
        self.var = "Inside constructor of class A"
        self.classvar1 = 'Inside Constructor of class A'

class B(A):
    classvar1 = "Class Variable of Class B"
    def __init__(self):
        super().__init__()
        self.classvar1 = "Inside constructor of class B"
        self.var2 = "Inside constructor of class B"
        # super().__init__()  # This will override the variables created before

        # using 'super()' to access super class variables and methods.
        '''Can access super class' attributes and method like this.'''
        print('Accessing super class\' variable',super().classvar1)

a = A()
b = B()

# print(b.var)
print(b.classvar1) # Different outputs when ran with B's constructor and without it.
# These are :-
# With constructor of B - output - Class variable of Class A.
# Without constructor of B - output - Instance variable of Class A.
# With constructor and super().__init__() - Instance variable of class A.

# If I run it without constructor of class B and overriding classvar1 in class B
# Ouput - Instance variable of class from constructor of class A because there is
# instance variable and it will got for it first


'''
Explanation - In the above example I created a class A and defined constructor and 
a class variable in it. Then I created class B and inherited it from class A.

>> Here, when I created constructor of in class B, I did not create self.var variable.
When I ran 'b.var' without constructor of class B, I got the value from instance 
variable from constructor of class A.

>> When I ran it with constructor of class B, 'b.var' I got an error because python
first searched it in instance variables did not find it and then went for class
variables, did not find it and then went to parent class and 
>>> "only searched for class variables because the constructor is being overridden in class B."
to access it I will have to use " super().__init__() " in class B's constructor.


>> If I don't define constructor of class B, then it will automatically run the constructor
of parent class.

>> If I define constructor of class B, then it will not run constructor of class A and
I will not get the instance variables created by class A's constructor.

>> Whenever I want to access a variable (whether class variable or instance one), 
it first searches for instance variable in the class, if doesn't find it, then
searches for class variable, if doesn't find it, then it goes to the parent class(s)
and again search in class variable and instance variable.

------------------------------------------------------------------------------------
Q. If I create an instance variable self.name and also a class variable "name",
I create an object, 'boy', which one will I get ?
Ans - I will get the instance variable, if it doesn't exist then only I will get the
class variable.
------------------------------------------------------------------------------------




'''


