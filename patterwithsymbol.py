n=int(input("enter the number of rows"))
for i in range(0,n):
    for k in range(0,n-i):
     print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()
