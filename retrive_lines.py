import re
f1=open('text1','r')
for i in f1.readlines():
    if(re.search('oo',i)):
        print(i)
