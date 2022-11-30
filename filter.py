# lst=[1,2,3,4,5,6,7,8]
# res=filter(lambda n:n%2==0,lst)
# print(list(res))


lst=input("enter the elements").split()
print(lst)
lst1=map(int,lst)
print(list(lst1))
res=filter(lambda n:n%2!=0,lst1)
print(list(res))
