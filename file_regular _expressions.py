import re
f1=open("text",'r')
for i in f1.readlines():
    if(re.search('THe',i)):
        print(i)