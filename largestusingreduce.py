from functools import *
lst=input("enter the list").split()
lst2=list(map(int,lst))
re=reduce(max,lst2)
print(re)