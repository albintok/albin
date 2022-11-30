x=int(input("enter the number"))
rev=0
A=x
while(x>0):
    d=x%10
    rev=(rev*10)+d
    x=x//10
print(rev)
if(rev==A):
    print("palindrome")
else:
    print("not palindrome")