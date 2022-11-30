import functools
def sum(*arg):
    for i in arg:
        re=functools.reduce(lambda x,y:x+y,arg)
    print(re)
sum(10,20,30)