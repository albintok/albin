
def small_cap(lst):
    uppercase = {}
    lowercase = {}
    uppercase['cap'] = 0
    lowercase['sml'] = 0
    for i in lst:
        if(i==" "):
            i.strip()
        elif(i.upper()==i):
            uppercase['cap']+=1
        else:
            lowercase['sml']+=1
    print(uppercase)
    print(lowercase)