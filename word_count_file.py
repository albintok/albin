f1=open('new_file','r')
lst=f1.read()
print(lst)
wordcount={}
for i in lst.split():
    if i not in wordcount:
        wordcount[i]=1
    else:
        wordcount[i]+=1
print(wordcount)
for k,v in wordcount.items():
    print(k,":",v)