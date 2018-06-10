def formarList(num):
    if isinstance (num,int) and (num>0):
        return pares(num)
    else:
        return "Número Incorrecto"

def pares(num):
    if num==0:
        return[]
    elif (num%10)%2==0:
        return Lista[num%10]+pares(num//10)
    else:
        return pares(num//10)
