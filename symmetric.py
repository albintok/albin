str=input("enter the string")
n=len(str)
if len(str)%2==0:
    mid=len(str)/2
    if(str[0:mid]==str[mid:n]):
        print("symmetric")
    else:
        print("not symmetric")
else:
    print("not symmetric")