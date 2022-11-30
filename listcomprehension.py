lst=['apple','orange','banana','kiwi']
newlist=[x for x in lst ]
print(newlist)
newlist2=[x for x in lst if 'b' in lst ]
print(newlist2)

lst=[x for x in range(0,9)]
print(lst)

lst1=['apple','orange','banana','kiwi']
lst3=[x if x=="kiwi" else "mango" for x in lst1]
print(lst3)