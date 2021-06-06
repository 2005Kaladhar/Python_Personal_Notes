'''
Scope and Global keyword in python

x = 45 # IT is a global variable and can be accessed by any function.
def func():
    print(x)
fun()

Output : 45
----------------------------Making a local variable for the function--------------------
x= 45

def func():
    x = 30
    print('Local variable "x": ',x)

func()
print("Global variable 'x':",x)

----------------------------------Using global keyword----------------

x = 45


def func():
    global x
    x += 5
    print("Priting from inisde of the function : ", x)


print("Printing Outside the function : ", x)
func()
print("Printing Outside the function after changing value: ", x)

Note - By default, all the global variables are available in read-only mode
to all the fucntions, to change the value of global variables, we need to
take the help of global keyword inside the function,

if the global keyword doesnt exist, it will create one in the Global Scope...-VVIMP.

--------------------------------------------------------------------------------
Q. What should I dot if I want to modify a global keyword at the same time
I want to create a local variable with the same name in my function ??
Ans - For this, we need to take help of another keyword called globals()
--------------------------------------------------------------------------------

1. We can get the read/write access of a global variable only in a single line.

x = 'global variable'
def func():
    x = 'Local variable'
    print(x) #It will print the local variable of the function.
    print(globals()['x']) #The access is limited to only this line.
func()
==>>Output:
Local variable
global variable

-------------------------------------------------------------------------------
2. understanding behaviour of global keyword in nested functions.

def func():
    x = 45 # local variable of func

    def func2():
        global x # It will create one if doesnt exist
        x = 30   # The variable in the global scope will be assigned this value.
        print("Printing from inside func2", x)

    print("INside function1,before calling func2,", x)
    func2()
    print("Inside function1, after calling func2", x)
    #Note - local variable of func() will not be affected at all.

print(x) # This will throw error because there no variable with name 'x'
func()
print("Printing from global scope", x) # Before func(), there was no 'x'

# Conclusion - While using global keyword in nested functions,it will not affect
the local variable of the upper function rather it will do operations on the variable
in global scope.

'''




