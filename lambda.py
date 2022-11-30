# syntax
# lambda argument:expression
# call using assigned value
# 
p=int(input("enter the principl"))
n=int(input("enter the period"))
r=int(input("enter the rate"))
simpl_interst=lambda p,n,r:(p*n*r)/100
print("simple interset is=",simpl_interst(p,n,r))