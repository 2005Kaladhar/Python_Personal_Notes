'''
            Understanding Multilevel Inheritance in Python

Multi level inheritance means, we keep inheriting classes. Once class inherits
another class and that class inherits from another class and so on...

For example -

class A:
    pass
class B(A):
    pass
class C(B):
    pass

Here, class C inherits class B and class B inherits class A.


Following is the example of multilevel inheritance.

'''
class ElectronicDevices:
    is_wireless = False
    portable = False

    def __init__(self,type,model_no,weight,cost):
        self.type = type
        self.model = model_no
        self.wht = weight
        self.price = cost
        self.max_volt_required = '5V'

    def print_details(self):
        print(f"Details : Type- {self.type}, Model- {self.model}, Weight- {self.wht}, Price-{self.price} ")

class PocketGadgegts(ElectronicDevices):
    portable = True
    ui = 'Basic'
    is_wireless = True

    name = "Portable Gadget"
    def setBattery(self,battery_life):
        self.battery_life = battery_life

    @classmethod
    def set_name(cls,name):
        cls.name = name

    @classmethod
    def set_wireless(cls,iswireless):
        cls.is_wireless = iswireless

    def print_details(self):
        print(f"Details : Name- '{self.name}', Type- {self.type}, Model- {self.model}")


class Phone(PocketGadgegts):
    ui = "Advance"
    can_play_games = True
    def set_new_attrib(self,internet_type):
        self.internet = internet_type

    def call(self,num):
        print(f"'{self.name}' calling to {num} using {self.internet} connection ..." )


television = ElectronicDevices('TV',123,'3Kg',10000)
radio = PocketGadgegts('Radio',4546,'400grams',600)
phone = Phone('Mobile Phone',4545,"200gram",15000)

phone.set_new_attrib('4G')
phone.set_wireless(True)
phone.set_name('Nokia')
phone.max_volt_required = '3.7V'

print('Is phone wireless ? :',phone.is_wireless)

phone.print_details()
print(f"Voltage requirement of Phone '{phone.name}' -> {phone.max_volt_required}")
phone.call('+91786453435')

print(f"Is TV wireless ? : {television.is_wireless}")
television.print_details()

print(f"Is Radio wireless ?? : {radio.is_wireless}")
radio.print_details()

