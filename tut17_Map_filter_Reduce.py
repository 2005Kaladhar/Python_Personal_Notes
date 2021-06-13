''' 
Undestanding map, filter and reduce functions.
-------------------------------------------------
1. map function

Q. What is the need of map function ??
Ans - If we are given an iterable and asked to apply a function
on each element of the iterable then we will definitely go for 
loops. 
But running loops for every task is not a good thing in our program
as this may cause some delay in our program and inefficient usage of
memory.

To do this task, we take the use of map function.

For example - We want to run int() function on each element of 
a list containing strings of numbers.

---------------------------------------------------------
a = ['1','2','3','4','5','6','7','8']

print('string of numebers ',a)
for i in range(len(a)):
    a[i] = int(a[i])

print('int of numbers ',a)

Output - 
string of numebers ['1', '2', '3', '4', '5', '6', '7', '8']  
int of numbers [1, 2, 3, 4, 5, 6, 7, 8]
-----------------------------------------------------------

Do the above task with map function

a = ['1','2','3','4','5','6','7','8']
print('string of numebers ',a)

a = list( map(int,a) )

print('int of numbers ',a)

Output -  (Same as previous program)
string of numebers ['1', '2', '3', '4', '5', '6', '7', '8']  
int of numbers [1, 2, 3, 4, 5, 6, 7, 8]
-----------------------------------------------------------

----------------------------------------------------------------------------------
-----------------------------Understanding map() function--------------------------
1. map function - "single function, multiple iterables"

syntax of map() :-  map(function_name,*iterable)

# Note - It is written '*'with iterable, it means that we can pass as many iterables as we 
want but the condition is that the function given to map() should accept as many no. of arguments
as we are providing the no. of iterables to it. (Will discuss further in this note.)


Things to remember about map() function :-
-------------------------------------------
1. In python2, map() returns a list, whereas in python3 it returns an object. This object can
be converted to list using list() or to a tuple using tuple().

2. While giving a function and iterables to map(), we need to make sure that the no. of 
arguments accepted by the function must be equal to the number of iterables given to map().


For example - I have a list of names of my friends in random case, I want it to be in such 
a way that the first letter if capital and rest are in small.

1. Using loop
---------------
friends = ['mohan','rAm','sHYam','roHit','raJenDra']

for name in friends :
    friends[friends.index(name)] = name.capitalize()
    
print(friends)

Output -  ['Mohan', 'Ram', 'Shyam', 'Rohit', 'Rajendra']

-------------------------------------------------------------------------------------
2. Using map() function 
-------------------------

friends = ['mohan','rAm','sHYam','roHit','raJenDra']

friends = list(map(str.capitalize ,friends))  # Don't give str.capitalize() [X] ERORR
 
print(friends)

Output - ['Mohan', 'Ram', 'Shyam', 'Rohit', 'Rajendra']


Note - While providing a function to map(), do not call the function like func_name(), just
give the name of the function, map() function will internally call the function when required.

-----------------------------------------------------------------------------------

In the above example, note that str.capitalize() just takes one argument so we gave it only
one iterable.

Let us take an example in which the function takes two arguments, then we will have to give
two iterables to map() function.

Example - 
--------

def func(name,roll_no):
    return f'{roll_no} -> {name}'
    
friends = ['Mohan', 'Ram', 'Shyam', 'Rohit', 'Rajendra']
roll_no = [i for i in range(1,11)]

name_roll = list(map(func,friends,roll_no))

for item in name_roll:
    print(item)
----------------
Output - 
1 -> Mohan
2 -> Ram
3 -> Shyam
4 -> Rohit
5 -> Rajendra


Explanation - In the above code, we made a function name 'func' which takes two arguments
'name' and 'roll_no' and returns a string with the name and the roll no. 

> While calling map() function, we passed the function name 'func', then the list of names
'friends' and then the list containing the rollno. 'roll_no'

> Internally, in one iteration, map function will give the first element of 'friends' list 
and first element of 'roll_no' list to 'func' function, in second iteratino, second element
of the lists will be given to 'func' as arguments.

> The sequence of iterables is obviously important as per the positions of arguments taken by the
'func' function.
If we would have changed the sequence of iterables, then we would have got this result 

name_roll = list(map(func,roll_no,friends))

Output - 

Mohan -> 1
Ram -> 2
Shyam -> 3
Rohit -> 4
Rajendra -> 5

Example2 - Q.Given a list of floating point numbers, round off all the floats such that
they have the same number of digits after decimal as their position are.
for example the first elements will be make to have one digit after decimal, second element
will have two digits after decimal.
---------Code------------------
g_floats = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013] 

rounded_ = list(map(round,g_floats,range(1,len(g_floats)+1)))
print(rounded_)

Output - [3.6, 5.58, 4.009, 56.2424, 9.01344, 32.00013]
-------------------------------------------------------
> In the above example, I have used round() function which takes a number an rounds it.
It also takes an optional second argument which is the number of digits after decimal.

> While defining map() function, I passed 'round', then list of floats 'g_floats' and then
the range function which generates a list of numbers from 1 to length of g_floats, it is 
written 'len(g_floats)+1' because range function generated upto 'n-1'.


Q. What if, the number of elements in the iterables given to map() function is different??
What will if in previous program we write

rounded_ = list(map(round,g_floats,range(1,10000) ) ) ??

Ans - map() function will not raise any error if the number of elements of the given iterables 
is different. It will run until it finds the suitable number of arguments to give to the function.
If a point comes where it has only one argument, i.e. elements of one list are finished, then
it will simply return the result.

The output of the previous code will then be - [3.6, 5.58] 


==> Understanding zip() function and making own zip function with map() 

. zip() - zip() function takes iterables and then it creates a tuple such that it will contain
all the elements of the iterables.
For example - 

list1 = [1,2,3,4,5]

my_strings = ['a', 'b', 'c', 'd', 'e']

fun = list(zip(list1,my_strings))
print(fun)

Output - [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
It created list of tuples such that the first tuple contains first element of list1 and first 
element of my_strings, second tuple containds second element of list2 , second element of 
my_strings and so on.....


> zip() function can take as many iterables as we want, and then it will do the same, create 
a tuple containing first elements of all the iterables, second tuple containing second element
of all the iterables.

==> Making own zip() function with map() function.


list1 = [1,2,3,4,5]

my_strings = ['a', 'b', 'c', 'd', 'e']

fun  = list( map( lambda x,y : (x,y), list1, my_strings ) )
print(fun)

Output - [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

------------------------------------------------------------------------------------------------
--------------------------------Understanding filter() function------------------------------------

2. Understanding filter() function. - "single function, single iterable"


> filter() - filter() function is used to create a list of elements which when passed to a function
return True.

Just like map() filter also take the name of a function an iterable. It passes all the elements
of the iterables to the function and saves the element if the function returns True on that 
element of the iterable.

For example - 
------------------------------
We want to filter out all the even numbers from this list 

numbers = [456,4354,31347,1321,465,2178,354,13,241435,313154]

all_evens = list(filter(lambda x : not bool(x%2), numbers))
print(all_evens)

Output - [456, 4354, 2178, 354, 313154]
--------------------------------------
--------------------------------------

==> VVIMP Differences Between map() and filter()

> Just like map() function, filter also returns a generator object which can be converted to list
or tuple using list() and tuple().

> map() can take multiple iterables provided that the function given should take that no. of 
arguments, but in filter() it takes only one iterable and it is compulsory (implicit) that the 
function should take only one argument and return a boolean value.

> In filter() if the function provided doesn't return a boolean value, then it returns the 
iterable itself without doing anything to it.


--------Making a Palindrome Detector with filter()--------------------
. Palindrome is a string which reads same backwards as forwards, for example - 'NAYAN'

. To verse a string we can use string slicing as -> string[::-1]

-------------------
Code - 
--------------------
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda x : x == x[::-1], dromes ))

print("Previous list -",dromes,"\nPalindromes sorted - ",palindromes)
--------
Output - 
---------

Previous list - ('demigod', 'rewire', 'madam', 'freer', 'anutforajaroftuna', 'kiosk') 
Palindromes sorted -  ['madam', 'anutforajaroftuna']

---------------------------------------------------------------------------------
-------------------------------Understanding reduce() function--------------------------------------------------

3. Understanding reduce() function. "single function, single iterable, returns a single value"

. map() and filter() are inubuilt functions avaible in python, but to use reduce() we need 
to import it from functools module.


. Unlike map() and filter() function, reduce function doesn't return an object. 
It returns a value.

Syntax of reduce - 
reduce(function_name, iterable, initial)

. reduce() - reduce() is used to perform a cummulative calculation on elements of a list.
For example if we are given a list, say a = [1,2,3,4,5] and we need to find the sum of all the
elements, then in that case we may take the help of reduce().

. In reduce() the function_name that we provide must be a function which takes exactly two 
arguments.

. The 'initial' represents the initial value from which the reduce() function will start.

. In general when initial is not given, it takes first and second element of the iterable and then
pass them to the function provided and then the value returned by the function and the next(third)
element of the iterable is taken and passed to the function, this is continued till all the elements
finish in the iterable.

For example - 
Finding sum of all the elements of a list using reduce() function.

----------Code----

from functools import reduce

a = [1,2,3,4,5]
add = lambda x,y : x+y

sum_of = reduce(add, a)  # It will return a value

print("Sum of all the elements in the list is ->",sum_of)
--------------------------------
Output  - Sum of all the elements in the list is -> 15
-----------------------------------

Explanation - 
In the above code when reduce() function iterates over the list, the following logic is applied

1. In first iteration, it takes first and second element of the iterable and passes them
to the function provided, the function adds them 

First element - 1, Second Element - 2
Passed to the function  - add(1,2)
Function Returned  - 3

2. In second iteration, the value returned by the function in the previous iteration is 
given as the first argument to the function and third element of the iterable is given as
second argument of the function.

First argument - 3
Second argument - third element of the list - 3
Passed to the function - add(3,3)
Function Returned - 6

And this process continues...till the iterable is completed and finally we get the result '15'.


==> Specifying 'initial' in reduce.
Taking the previous code 

----------Code----

from functools import reduce

a = [1,2,3,4,5]
add = lambda x,y : x+y

sum_of = reduce(add, a, 15)  # It will return a value

print("Sum of all the elements in the list is ->",sum_of)
--------------------------------
Output  - Sum of all the elements in the list is -> 30
-----------------------------------

. When I specified 'initial', it took '15' as the initial value, tool the first element of the iterable
and then passed the initial and the first element to the functin instead of passind first and second 
element of the iterable to the function.

Hence the result became '30' because it started with 15 as initial value and it also got added to the 
actual sum of the list. Thus it became --> '15' (as previous output) + 15 ('initial' specified)


================== Finding factorial of a given number with reduce() function==============
from functools import reduce 
inp = int(input("Enter the number to find factorial : "))

fact = reduce(lambda x,y: x*y, range(1,inp+1))

print(f"Input - [{inp}] and {inp}! = {fact}")

---------------------
Output - 
-----------
Enter the number to find factorial : 5
Input - [5] and 5! = 120



'''


from functools import reduce
print("Small Exrecise taken from learnpython.org")

# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

my_floats = list(map(lambda x : round(x*x,3),my_floats ))
print("Square of the given list rounded to three decimal value is ->",my_floats)

# Use filter to print only the names that are less than 
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
my_names = list(filter(lambda x :len(x)<=7,my_names) )
print("Names which have letters less than or equal to 7 is ->",my_names)

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]
my_numbers = reduce(lambda x,y : x*y, my_numbers)
print("Product of all the numbers in the give list is ->",my_numbers)


# Finding factorial of a given number using reduce() function from functools

inp = int(input("Enter the number to find factorial : "))

fact = reduce(lambda x,y: x*y, range(1,inp+1))

print(f"Input - [{inp}] and {inp}! = {fact}")



