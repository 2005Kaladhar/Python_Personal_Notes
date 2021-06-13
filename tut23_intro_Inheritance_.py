'''
=================== Inheritance in OOPS ===============================

Pillars of OOPS

1. Abstraction.
2. Encapsulation.
3. Polymorphism.
4. Inheritance.

Encapsualtion - Hiding the implementation of work
Asbstraction  - Breaking down a task into simpler tasks. 

---------------------------------------------------------------------------
>> Types of inheritance in Python

1. Single inheritance       - A class inherits only one class
2. Multi level inheritance  - Classes keep inheriting.. bacche ka bacche ka baccha ....
3. Multiple inheritance     - Single class inheriting more than one class.
4. Hierarchical Inheritance - Creating multiple child classes from one base class.
5. Hybdrid inheritance      - Involving different types of inheritance
---------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------
                            Single level inheritance in Python

Inheritance in OOPS is just like the normal law of inheritance in nature, just like
children have similar characteristics of their parents, child class also inherits
methods and attributes of parent class.

______COde______
class Operating_system:
    creator = "Kaladhar Gopal"
    credits = "ThunderBolt Industries"

    def __init__(self,os_name,kernel,architecture,version):
        self.os_name = os_name
        self.architecture = architecture
        self.version = version
        self.kernel = kernel

    @classmethod
    def creator_changer(cls,new_creator):
        cls.creator = new_creator

    def print_details(self):
        return f'Os-{self.os_name}, Kernel-{self.kernel}, Version-{self.version}, ' \
               f'Architecture-{self.architecture}, Creator-{self.creator}'

class Windows(Operating_system):
    pass

windows = Windows('Windows10','WindowsNT','64Bit',10)
details = windows.print_details()
print(details)

windows.creator_changer('Gopal')
#Changing creator name
print(windows.print_details())

---------------------------
Output -
Os-Windows10, Kernel-WindowsNT, Version-10, Architecture-64Bit, Creator-Kaladhar Gopal
Os-Windows10, Kernel-WindowsNT, Version-10, Architecture-64Bit, Creator-Gopal

---------------------------
Explanation - In the above example, we created a class named Operating_system and then
created another class named Android and inherited it from Operating_system class.

>> As we inherited it, all the methods and attributes got inherited even the constructor.
# Note - When we inherit a class, the child class inherits even the constructor of the
parent class.

>> We can access the methods and attributes from child class. We can also modify the
methods and attributes or we can override those methods and attributes in child class.


=========================================================================================
                            Overriding Constructor in child class

_____COde________
class Operating_system:
    creator = "Kaladhar Gopal"
    credits = "ThunderBolt Industries"

    def __init__(self,os_name,kernel,architecture,version):
        self.os_name = os_name
        self.architecture = architecture
        self.version = version
        self.kernel = kernel

    @classmethod
    def creator_changer(cls,new_creator):
        cls.creator = new_creator

    def print_details(self):
        return f'Os-{self.os_name}, Kernel-{self.kernel}, Version-{self.version}, ' \
               f'Architecture-{self.architecture}, Creator-{self.creator}'

class Windows(Operating_system):
    def __init__(self,os_name,kernel,architecture,version,dual_boot):
       self.os_name = os_name
       self.architecture = architecture
       self.version = version
       self.kernel = kernel
       self.dual_boot = dual_boot

    # Overriding a function of parent class
    def print_details(self):
        return f'Os-{self.os_name}, Kernel-{self.kernel}, Version-{self.version}, ' \
               f'Architecture-{self.architecture}, Creator-{self.creator}\n' \
               f'Dual Boot - {self.dual_boot}'

windows = Windows('WIndows',"WindowsNT","64Bit",10,True)

details = windows.print_details()
print(details)


--------------------------------------------------------------------------
Output -
Os-WIndows, Kernel-WindowsNT, Version-10, Architecture-64Bit, Creator-Kaladhar Gopal
Dual Boot - True
------------------------------------------------------------------------

Explanation - In the above code, we again inherited Windows class from Operating system
class, and we overrode constructor and created a constructor for Windows class and there
I specified another argument to tell whether it is in dual boot or not
and then created instance variables.

# Note - BUt this is not the way of using OOPS and overriding the constructor.
>> IN the child class we can run the constructor of parent class with the help of a
function named 'super().__init__()'

-----------------COde----------------
class Windows(Operating_system):
    def __init__(self,os_name,kernel,architecture,version,dual_boot):
        super().__init__(os_name,kernel,architecture,version)
        self.dual_boot = dual_boot
------------------------------------


'''

class Operating_system:
    creator = "Kaladhar Gopal"
    credits = "ThunderBolt Industries"

    def __init__(self,os_name,kernel,architecture,version):

        self.os_name = os_name
        self.architecture = architecture
        self.version = version
        self.kernel = kernel

    @classmethod
    def creator_changer(cls,new_creator):
        cls.creator = new_creator

    def print_details(self):
        return f'Os-{self.os_name}, Kernel-{self.kernel}, Version-{self.version}, ' \
               f'Architecture-{self.architecture}, Creator-{self.creator}'

class Windows(Operating_system):
    def __init__(self,os_name,kernel,architecture,version,dual_boot):
        super().__init__(os_name,kernel,architecture,version)
        self.dual_boot = dual_boot

    # Overriding a function of parent class
    def print_details(self):
        return f'Os-{self.os_name}, Kernel-{self.kernel}, Version-{self.version}, ' \
               f'Architecture-{self.architecture}, Creator-{self.creator}\n' \
               f'Dual Boot - {self.dual_boot}'

windows = Windows('WIndows',"WindowsNT","64Bit",10,True)

details = windows.print_details()
print(details)






