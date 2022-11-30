def binarysearch(list,key):
    start=0
    end=len(list)-1
    mid=0
    while(start<=end):
        mid=(start+end)//2
        if(int(list[mid])<key):
            start=mid+1
        elif(int(list[mid])>key):
            end=mid-1
        else:
            return mid
    return -1

lst=input("enter the list").split()
lst.sort()
key=int(input("enter the key to be searched"))
res=binarysearch(lst,key)
if(res==-1):
    print("value not found")
else:
    print("value found at position",mid)