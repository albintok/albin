dic1={"no":1,"name":"albin"}
print(dic1)
print(dic1.keys())
print(dic1.values())
dic1["salary"]=30000
del dic1["name"]
print(dic1)
print(len(dic1))
print(dic1.items())
dic2={"adress":"house"}
dic1.update(dic2)
print(dic1)
