lst=input("enter then elements").split()
print(lst)
lst1=[]
lst2=[]
for i in lst:
    if int(i)%2==0:
        lst2.append(i)
    else:
        lst1.append(i)
print("even numbers are:",lst2)
print("odd numbers are:",lst1)