from functools import *
lst=[1,2,3,4,5]
res=reduce(lambda x,y:x+y,lst)
print(res)
res1=reduce(lambda x,y:x*y,lst)
print(res1)
res2=reduce(lambda x,y:x/y,lst)
print(res2)


