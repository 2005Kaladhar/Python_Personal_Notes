'''
===================== Understanding Multiple Inheritance ======================

>> We can inherit more than one class in a class.
This  is called Multiple Inheritance.

. While inheriting from more than one class, the order in which the classes
are inherited must be kept in mind.

MRO - Method resolution order
This is the order in which a child searches for a method or an attribute when it
inherits from multiple classes

Whenever we call a method or try to access an attribute of an instance
it first searches it in the class of instance if it doesn't find it, then
it searches in the parent classes, first in the class which is written first
and then the second class and so on. If it doesn't find the method or attribute in
any of the classes, it raises and Error.

________COde______
class Functions:
    def __init__(self,name,storage,ram):
        self.name = name
        self.storage = storage
        self.ram = ram

    def call(self,num):
        print(f"[{self.name}] -> Calling to {num}...")

    @classmethod
    def set_location(cls,location):
        cls.location = location


class Phone:
    def __init__(self,name,ram,price,storage):
        self.name = name
        self.storage = storage
        self.ram = ram
        self.price = price

    def print_details(self):
        return f'Name-{self.name}, RAM-{self.ram}, Storage-{self.storage}, Price-{self.price}' \


class SmartPhone(Phone,Functions):

    def __init__(self,name,ram,price,storage,processor,architecture):
        super().__init__(name,ram,price, storage)
        self.processor = processor
        self.architecture = architecture


nokia = SmartPhone('Nokia','8GB',15000,'128GB','SnapDragon360','64Bit')

nokia.set_location('Jamuna Colliery')
print(nokia.location)

nokia.print_details()
nokia.call(456789)

-------------------------------
Output -
Jamuna Colliery
[Nokia] -> Calling to 456789...
-------------------------------


Explantion - In the above code, we created a class named 'Functions' in which we defined
an instance method and a classmethod.
Next we created another class named Phone in which we created a constructor, and an instance
method.

Next we inherited Phone and Functions classes in Phone class.
In the constructor of Phone class, we called constructor of super class,
here comes the role MRO, method resolution order of SmartPhone class is

SmartPhone
Phone
Functions

It means that it first searches the method in SmartPhone class itself, if doesnt find
it then in Phone class and finally in Functions class when it doesnt find it in Phone class.

So, while calling super().__init__() it calls the constructor of Phone class which is
written first.

If we want to run the constructor of Function class, then we can run it as follows

Functions.__init__(arguments)


================================== VVIMP Note ======================================================
It is to be noted that in Functions class's call() method, we are using self.name, since
self.name instance variable in created by Phone class, it is running fine, but if it
would be something else like 'self.rname' which is created by the constructor of Functions class
then it would have thrown error because we are not running constructor of Functions Class.

'''
class Functions:
    def __init__(self,name,storage,ram):
        self.name = name
        self.storage = storage
        self.ram = ram

    def call(self,num):
        print(f"[{self.name}] -> Calling to {num}...")

    @classmethod
    def set_location(cls,location):
        cls.location = location


class Phone:
    def __init__(self,name,ram,price,storage):
        self.name = name
        self.storage = storage
        self.ram = ram
        self.price = price

    def print_details(self):
        return f'Name-{self.name}, RAM-{self.ram}, Storage-{self.storage}, Price-{self.price}' \


class SmartPhone(Phone,Functions):

    def __init__(self,name,ram,price,storage,processor,architecture):
        super().__init__(name,ram,price, storage)
        self.processor = processor
        self.architecture = architecture


nokia = SmartPhone('Nokia','8GB',15000,'128GB','SnapDragon360','64Bit')

nokia.set_location('Jamuna Colliery')
print(nokia.location)

nokia.print_details()
nokia.call(456789)





