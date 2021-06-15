'''
External Test line in python

        Diamond Shape Problem

Generally a programmer is advised to avoid multiple
inheritance as it give rise to many problems, one
such problem is "Diamond Shape Problem", in python
MRO (Method Resolution Order) can easily solve this
but in languages like Java and C++ it becomes very
much complicated.




'''


class A:
    def printer(self):
        print("Method from class A")
    pass

class B(A):
    # def printer(self):
    #     print("Method from class B")
    pass

class C(A):
    def printer(self):
        print("Method from class C")
    pass

class D(B,C):
    # def printer(self):
    #     print("Method from class D")
    pass

a = A()
b = B()
c = C()
d = D()

'''

First it searches in class D itself,
1. if doesn't find it then goes to class B (written first), 
2. if doesn't find then goes to class C,
3. if doesn't find then go to parent class of B
4. and then to parent class of C.

>> If B and C don't have it then ultimately it will
call the method from class A'''

'''
>> If B and C have printer() method, then it will
run the method of B only, because it is written first
while inheriting in class D.

>> If we write 
class D(C,D):
    pass
Then it will run printer() from class C

>> If class D itself has this method then it will 
run the its own method.

>>> VVIMP
If class B doesn't have the method, but class C has
then it will run the method of class C even when 
class A has it.

> Class A will be searched when class B and C don't have
the method.

'''
d.printer()



