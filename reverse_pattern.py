# n=int(input("enter the no.of rows"))
# for i in range(0,n):
#     for k in range(0,i+1):
#         print("8",end=" ")
#     for j in range(0,n-i):
#         print(end=" ")
#     print()



n=int(input("enter the number of rows"))
for i in range(n,0,-1):
    for k in range(n-i,0,-1):
     print(end=" ")
    for j in range(i,0,-1):
        print("*",end=" ")
    print()