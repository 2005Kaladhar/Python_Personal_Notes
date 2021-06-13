'''
Suppose we are given a list of some items that we want to buy from market
and we need to print the items in a readable format such that
each item is separated by ',' or 'and' , then we have two approaches to
solve this problem as follows :-

==> 1. Using Loops
-------------------
a = ['tamatar','daal','shakkar','haldi','gudh','aata']

print("You need to buy the following items : ")
for item in a :
    if item == a[-1]:  #If it is last item then do not add 'and' at end
        print(item)
    else :
        print(item,'and',end=' ')

==> Output :-
You need to buy the following items :
tamatar and daal and shakkar and haldi and gudh and aata,
-----------------------------------------------------
==> 2. Using .join() method in string

items = ['tamatar','daal','shakkar','haldi','gudh','aata']
a = ' and '.join(items)
print("You need buy the following items : ")
print(a)

# We got the same output with few lines of code.


==> Output :-
You need to buy the following items :
tamatar and daal and shakkar and haldi and gudh and aata
-----------------------------------------------------------


'''

