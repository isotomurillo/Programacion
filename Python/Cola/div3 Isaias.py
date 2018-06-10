def Div3 (num):
    if isinstance (num,int):
        return verif(num,0,0)
    else:
        return "Error"

    

def verif (num,new,pot):
    if num==0:
        return new
    elif (num%10)%3==0:
        return verif(num//10,new,pot)
    else: return verif (num//10,new +num%10*10**pot,pot+1)
