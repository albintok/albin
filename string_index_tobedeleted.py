str=input("enter the elemnets").split()
print(str)
n=int(input("enter the index to be deleted"))
print(n)
str2=str[0:n]+str[n+1:]
print(str2)