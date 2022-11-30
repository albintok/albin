def search(lst):
    for i in lst:
        if("a" in lst or "A" in lst):
            return True
        else:
            return False
lst=input("enter the list").split()
lst1=list(lst)
res=filter(search,lst1)
print(list(res))