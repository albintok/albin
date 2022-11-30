def linearsearch(list1,key):
    n=len(list1)
    for i in range(0,n):
        if(list1[i]==key):
            return i
    return -1
lst=[1,2,3,4,5,6,7,8,9]
key=5
res=linearsearch(lst,key)
if(res==-1):
    print("not found")
else:
    print("item found at index",res)