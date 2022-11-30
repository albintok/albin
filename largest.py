lst=input("enter the list").split()
lst2=list(map(int,lst))
print(lst2)
lar=0
for i in lst2:
    if(i>lar):
        lar=i
    else:
        continue
print(lar)
