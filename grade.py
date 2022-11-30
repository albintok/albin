x=int(input("enter mark1"))
y=int(input("enter mark2"))
z=int(input("enter mark3"))
if(0<x<100 and 0<y<100 and 0<z<100):
    avg=((x+y+z)/300)*100
    print("average is=",avg)
    if(avg>80):
     print("a+")
    elif(60<=avg<=80):
     print("b+")
    elif(50<=avg<=60):
     print("c")
    else:
     print("failed")
else:
    print("enter mark less than 100")