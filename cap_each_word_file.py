f1=open('text','r')
lst2=[]
str=" "
lst=f1.read()
for i in lst:
    if(i.upper()!=i):
        lst2.append(i.upper())
    else:
        lst2.append(i)
for i in lst2:
    str+=i
print(str)
f1.close()