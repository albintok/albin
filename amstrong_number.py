sum=0
x=int(input("enter the number"))
sum=0
num=x
n=len(str(x))
print(n)
while(x>0):
    d=x%10
    sum=sum+(d**n)
    x=x//10
print(sum)
if(sum==num):
    print("its a amstrong num")
else:
    print("its not a amstong num")