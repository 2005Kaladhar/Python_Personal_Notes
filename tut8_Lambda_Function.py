'''
Anonymous function.(Lambda Function)
Lambda function is used to create one liner functions.

-----------------------------------------------------------
def add(a,b):
    return a+b

add = lambda a,b : a+b #This will work same as the above defined function.
-------------------------------------------------------------------------

==> Using lambda function with .sort() method.

.sort() is used to sort an iterable with the help of a function.
It takes an argument named 'key' to sort the given list.

Note - while giving arguments to .sort() method make sure that you give
keyworded arguments rather than positional arguments because it doesnt take
positional arguments.

def function(x):
    return x

a = ['Santosh', "Ankush", 'Yog', "Pranjal"]
print("List before sorting the list: ", a)

a.sort(key=function, reverse=False)  # By Default reverse=False
print("List after sorting the list: ", a)

-------------------Making with lambda function----------------------------
a.sort(key=function, reverse=False)  # By Default reverse=False
print("List after sorting the list: ", a)


-------------------------------------------------------------------------------
Diving deep into lambda functions.
In different programming languages, it is known by different names -
. Anonymous Functions
. Lambda Functions
. Lambda Expression
. Lambda Abstractions
. Lambda Form
. Function Literals

Two approaches to use lambda function.
1. Either create one liner functions.
2. Pass the lambda function to another function.

Immediately executing lambda function.
IIFE - Immediately Invoked Function Expression
We can invoke a lambda function at the time of defining it.
In that case we need not declare a variable for it and hence the functino
actually remains anonymous.

(lambda x,y:print(x+y) )(15,20)
Output: 35

--------------------------------------------------------------------------------
Another interesting example of lambda function
super_function = lambda x,func:x+func(x)
chotu_function = super_function(2,lambda y:y+8)
print(chotu_function)
Output : 12

----------------------------------------------------------------------------------
==>Spanning lambda function to multi lines

a = (lambda x:
 print(f"Hello world this is {x}") )
#We can define a multiline lambda function as mentioned above

#Calling the function
a('kaladhar gopal')

----------------------------------------------------------------------------------
==> Types of Arguments in Lambda function.
Just like a normal function (made with def) lambda function also supports all types
of arguments.

1. Positional Arguments - normally used
2. Keyword Arguments
3. Default Arguments
4. Variable Length Argument - *args
5. Keyworded Variable Lenght Argument - **kwargs

1.
a = lambda x,y: x+y
print(a(4,5))

2.
a = lamda first_name, last_name: print(f"{first_name} {last_name}")
a('kaladhar','gopal')

3.
a = lambda list_,want_reverse=False : list_.sort(key= lambda x:x ,reverse=want_reverse)
b = ['Yog','Ankush Aditya',"Ankush Marko","Deepak"]

a(b)
print(b)

4.
a = (lambda *args : print(args) )
b = a('kaladhar','gopal','monu')[1]
print(b)

5.
a = (lambda name,**kwargs: print(f'Name is {name}, rest is {kwargs}') )
a('Kaladhar',role='student',age=16,income=10**100)


'''




