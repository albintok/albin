import itertools
lst=[1,2,3,4,5]
re=itertools.accumulate(lst,lambda x,y:x+y)
print(list(re))