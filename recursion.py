# n=int(input("enter the number"))
# def fact(n):
#     if(n==1):
#         return 1
#     else:
#         return n*fact(n-1)
# factorial=fact(n)
# print(factorial)


n=int(input("enter the number"))
s=0
def sum(n):
    if(n==0):
        return s
    else:
        return s*sum(n-1)
sumof=sum(n)
print(sum)
