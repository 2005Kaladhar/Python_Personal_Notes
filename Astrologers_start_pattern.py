#Solution by Kaladhar Gopal
n = int(input("Enter the no. of lines of the pattern : ") )
#The style in which the user wants to print the pattern
style = bool(int(input("To print, \nupside down - 0 \nnormal - 1\nYour Choice : ")))

#Default settings for 'for-loop'
start,stop,step = 1, n+1,1

#Settings will change if user wants to print it upsidedown.
if not style:
    start,stop,step = n,0,-1
#Finally printing the pattern according to user.
for i in range(start,stop,step):
    print('*'*i)
#If user gives no. of lines as 0 then this else suite will run
else:
    print("Ha ha ha :) Kya Majak Kar rahe ho yrr!!")