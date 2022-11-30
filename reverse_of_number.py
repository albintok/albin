x=int(input("enter the number"))
rev=0
while(x>0):
    d=x%10
    if(d==0):
        print(d,end="")
    rev=(rev*10)+d
    x=x//10
print(rev)