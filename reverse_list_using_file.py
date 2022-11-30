f1=open('text','r')
lst=f1.readlines()
print(lst)
lst1=lst[::-1]
print(lst1)
for i in lst1:
    print(i.strip())
f1.close()