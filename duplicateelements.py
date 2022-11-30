lst=input("enter elemts").split()
print(list(lst))
lst2=list(map(int,lst))
print(lst2)
for i in lst2:
    if i not in lst2:
        new.append(i)
print(new)