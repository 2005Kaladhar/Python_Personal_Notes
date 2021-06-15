'''
         Understanding getters setter and property decorator

The main purpose of using getters and setters (property) function is to uphold the
concept of Encapsulation.
We actually hide the implementation inside a class.

Situations where we use getters and setter -
1. To get and set the value of private variables
2. To add validation logic in getting and setting a value.

For example - If we have a class named student and we have his bank account no. stored in a private
variable, then to set and get the account no. we can use property function to define the getter and
setter and also a deleter, we can also write a validation logic while getting, setting and deleting
the value.

_______Code________
class Student:
    def __init__(self):
        self.__bank_account = 41354135

    def get_bank(self):
        print("Getter function called")
        return self.__bank_account

    def set_bank(self,values):
        print("Setter method called")
        # print(password)
        if values[0] == "kaladhar":
            print("Password Verified")
            self.__bank_account  = values[1]
        else:
            raise AssertionError("The Password Given was not correct")

    def del_bank(self,values):
        print("Deleter function called")
        if values[0] == "kaladhar":
        print("Password Verified")
            del self.__bank_account
        else:
            raise AssertionError("The Password Given was not correct")

    bank_account = property(get_bank, set_bank, del_bank)


kaladhar = Student()

kaladhar.bank_account = "kaladhar",123456789

print(kaladhar.bank_account)

---------------------------------------------------------------
Output -
Setter method called
Password Verified
Getter function called
123456789
---------------------------------------------------------------

Explanation - In the above code, in Student class, we have a private variable which has
bank account number of the student. To get and set the value of this private variable
we could have used normal instance methods, but they would not have any special implementation.

>> If we observe the code, then we'll find out that to get set and delete bank_account, we
are using an attribute "bank_account" which is not defined in the class, this is made to
store property function and it is acting like an attribute.

>> Property function takes four arguments - fget- to_get, fset-to_set, fdel-to_delete and
doc - to create docstring for an attribute.

>> In the property function we passed the names of our functions doing these tasks.
Whenever assignment operator is used to set the value of "bank_account", "fset" is called
when we want to access the attribute, then "fget" is called and when we delete 'bank_account'
fdel is called.

>> Further we can add validation logic while getting or setting the value, in the above code,
while setting the value we are also taking a password and if the password matches the pre-defined
password then it sets the value.

>> While assigning 'bank_account' prpoerty function calls 'fset' and whatever we assign to 'bank_account'
is given to 'fset unction as tuple(basically like *args) and we can use it to have two values while
assigning the value, first will be the password and second will be the value to be assigned to '__bank_account'
when the password matches otherwise it will raise AssertionError.


# NOte - A property object creates and return three methods - getter(), setter() and delete()

-----------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------

==========================  Using property as a decorator =============================================

>> Another way of implementing property function is to use it as a decorator.
Just make the getter method with @property decorator and then for other
methods just specify like  @func.deleter(), @func.setter() like this.

>> Suppose we make the method to set variable with @property decorator and try to do
@func.getter then other methods will not run properly, therefore always use @property decorator
on the method which is to be made as getter method.


________COde___________
Re-writing the previous code using property decorator.

class Student:
    def __init__(self):
        self.__bank_account = 41354135

    def get_bank(self):
        print("Getter function called")
        return self.__bank_account

    def set_bank(self,values):
        print("Setter method called")
        # print(password)
        if values[0] == "kaladhar":
            print("Password Verified")
            self.__bank_account  = values[1]
        else:
            raise AssertionError("The Password Given was not correct")

    def del_bank(self,values):
        print("Deleter function called")
        if values[0] == "kaladhar":
            print("Password Verified")
            del self.__bank_account
        else:
            raise AssertionError("The Password Given was not correct")

    bank_account = property(get_bank, set_bank, del_bank)

kaladhar = Student()

kaladhar.bank_account = "kaladhar",123456789

print(kaladhar.bank_account)

'''

class Student:

    def __init__(self):
        self._bankAC = 123753

    @property
    def bank_account(self):
        print("Getter method is called")
        return self._bankAC

    @bank_account.setter
    def bank_account(self, value):
        print("Setter method is called")
        if value[0] == 'kaladhar':
            print('Password Verified... ')
            self._bankAC = value[1]

    @bank_account.deleter
    def bank_account(self,value):
        print("Deleter method is called")
        if value[0] == 'kaladhar':
            print("Password verified...")
            del self._bankAC

kaladhar = Student()

print(kaladhar.bank_account)

kaladhar.bank_account= 'kaladhar',456789

'''
Single level inheritance
Multi level inheritance
multiple inheritance
Getters setters and property decorator

polymorphism in python
- Inbuilt polymorphic functions
- Duck Typing / User defined polymorphic functions
- Method overloading
- Method overriding 
- Polymorphism in inheritance.





'''

