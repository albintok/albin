def dec_fun(fun):
    def inner_fun(n1,n2):
        if(n1<n2):
            (n1,n2)=(n2,n1)
        return fun(n1,n2)
    return inner_fun



@dec_fun
def sub(n1,n2):
    return n1-n2
@dec_fun
def div(n1,n2):
    return n1/n2
print(div(2,10))
print(sub(2,10))