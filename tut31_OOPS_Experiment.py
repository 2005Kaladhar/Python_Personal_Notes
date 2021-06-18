'''
Experimenting with getters setters and property decorator.

''' 
class Employee:
    employees = []
    def __new__(cls,*args):
        instance = object.__new__(cls)
        cls.employees.append(f"{args[0]} {args[1]}")

        return instance
        
    def __init__(self,fname,lname,salary,role):
        self.salary = salary
        self.role = role

        self.fname = fname
        self.lname = lname

        self.email = f"{self.fname}_ThunderBolt_{self.lname}@gmail.com"
        self.__password = hash(self.fname+str(self.salary)[0])
    
    @classmethod
    def alter_constructor(cls,string) :
        return cls(*string.split(' '))

    @property
    def name(self) :
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self,new_name) :
        splitted = new_name.split(' ')
        self.fname = splitted[0]
        self.lname = splitted[1]
        self.email = f"{splitted[0]}_"\
            f"ThunderBolt_{splitted[1]}@gmail.com"

    @name.deleter
    def name(self):
        del self.name
    
    @property
    def password(self):
        pass

    @password.setter
    def password(self,val):
        prev_pass = val[0]
        new_pass = val[1]
        if hash(prev_pass) == self.__password:
            self.__password = hash(new_pass)
            print(f"New password has been set.. for {self.fname}")
        else:
            print("ERROR - Prev Password Is not in Database.")

    
    def pass_check(self,raw_val):
        if self.__password == hash(raw_val):
            print(f"Password Matched for {self.fname}")
        else:
            print(">> ERROR : PSWD incorrect")


    def print_details(self):
        print(f"Name is {self.name}, Salary is {self.salary},"\
            f" Role is {self.role}")


    def __add__(self,other):
        print(other)
        # return self.salary + other.salary 

kaladhar = Employee.alter_constructor ("Kaladhar Gopal 123 Programmer")
gopal    = Employee.alter_constructor ("Gopal Kaladhar 321 Developer")
rohan    = Employee.alter_constructor ("Rohan KUmar 213 Engineer")

print(Employee.employees)

kaladhar.pass_check('Kaladhar1')
kaladhar.password = 'Kaladhar1','kaladhargopal'

kaladhar.pass_check('kaladhargopal')

print(kaladhar.email)

