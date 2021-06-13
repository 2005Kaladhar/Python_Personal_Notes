'''
Understanding enumerate function for a sequence of elements,
(tuples,lists).

enumerate function returns an enumerate object which can be
converted to list.
THe object contains tuple of index of element and the element.
The enumerate object can be converted to a list.

For example - If we are given a list of elements and we are
supposed to print only the element which are at odd positions,
then we may have two methods of solving this problem.

1. The traditional method.

a = ['aalo','pyaz','tamatar','tori','tinde','kachori']

for i in a :
    if not (a.index(i)+1) %2:
        print(i)
-------------------------------------------------------------
2. Using enumerate function.

a = ['aalo','pyaz','tamatar','tori','tinde','kachori']

for index,element in enumerate(a):
    if not (index+1) % 2:
        print(element)



'''








