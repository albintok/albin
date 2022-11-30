def sum(a,b):
    s=a+b
    return s
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    m=a*b
    return m
def diff(a,b):
    d=a/b
    return d
print("menu driven program")
a=int(input("enter the element"))
b=int(input("enter the element"))
while True:
    print("1.Addition")
    print("2.substraction")
    print("3.multiplication")
    print("4.division")
    print("5.Exit")
    ch=int(input("enter your choice"))
    if(ch==1):
        s=sum(a,b)
        print("--sum is--=",s)
    elif(ch==2):
        c=sub(a,b)
        print("--differnce is--=",c)
    elif(ch==3):
        m=mul(a,b)
        print("--product is--=",m)
    elif(ch==4):
        d=diff(a,b)
        print("--quotient is--=",d)
    elif(ch==5):
        break
    else:
        print("enter correct choice")