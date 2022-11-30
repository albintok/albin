str=input("enter the string")
n=int(input("enter the position to be removed"))
print(str)
print(n)
str1=" "
lst=list(str)
lst.pop(n)
for i in lst:
    str1+=i
print(str1)