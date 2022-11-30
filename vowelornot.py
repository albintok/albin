x=input("enter the string")
v=0
c=0
s=0
vowl=[]
spaze=[]
consont=[]
for i in x:
    if i in "aeiouAEIOU":
        v=v+1
        vowl.append(i)
    elif(i==" "):
        s=s+1
        spaze.append(i)
    else:
        c=c+1
        consont.append(i)
print("no.of vowels in",x,"is",v,end=" ")
print(vowl)
print("no.of spaces in",x,"is",s,end=" ",spaze)
print("no.of consonats in",x,"is",c,end=" ",consont)