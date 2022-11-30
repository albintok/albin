#lst=['1','2','3','4','5']
# lst1=map(int,lst)
# print(list(lst1))

# using function
# def square(n):
#     return n*n
# lst=[1,2,3,4]
# res=map(square,lst)
# print(list(res))


#using lambda fun

# squre=lambda n:n*n
# lst=[1,2,3,4,5]
# res=map(squre,lst)
# print(list(res))


# lst1=[1,2,3,4,5]
# lst2=[6,7,8,9,10]
# res=map(lambda a,b:a+b,lst2,lst1)
# print(list(res))


lst=['sat','bat','hat']
res=map(lambda x:list(x),lst)
print(list(res))
