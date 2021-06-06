'''
While working in python we may come across many terminologies when it comes
to import something in your code. These are -
1. Module
2. Package
3. Library

----------------------------------
Module - It is a python file containing functions, global variables etc.
        To organise many modules, we have packages.
----------------------------------
Package - It is a directory containing multiple modules. One way to identify
        a module is to search for a ___init__.py file as all the modules have it.
-----------------------------------
Library - It is a collection of related functionality of code which allows you to
        perform a particular task without writing the code. In a nutshell, library is
        something which does something for us without writing code to perform the task
        from scratch.
---------------------------------
for example -
We have pandas library for data manipulation and analysis.

import pandas as pd
df = pd.read_csv("file_name.csv")




'''

# ---------------------Using time and datetime module--------------------------
from datetime import date
import time

today_ = date.today()
iso_clndr = date.isocalendar(today_)

time_ = time.asctime(time.localtime())

print(today_,'\n',time_,sep='')

print(f"Waiting for a second ",time.sleep(1000))
print(iso_clndr)









