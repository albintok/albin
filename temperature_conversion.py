print("Temperature conversion")
print("1.celcuis to farenheit")
print("2.farenheit to celcius")
choice=int(input("enter your choice"))
if(choice==1):
    c=float(input("enter the temperature in celcius"))
    f=(9/5)*c+32
    print(f)
elif(choice==2):
    f=float(input("enter the temperature in farenheit"))
    c=(5/9)*(f-32)
    print(c)
else:
    print("enter correct value")
