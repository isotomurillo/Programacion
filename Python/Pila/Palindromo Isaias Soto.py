def palindromo (num):
    if isinstance (num,int) and (num>0):
        return poten(num,0,num)
    else: return "Número no válido"

def poten(num,cont,numero):
    if num==0:
        return 0
    elif num>10:
        return poten(num//10,cont+1,numero)
    else:
        return verif(numero,cont,numero)

def verif(num,pote,numero):
    if num==0:
        return 0
    else:
        return compa(((num%10)*(10**pote))+verif(num//10,pote-1,numero),numero)

def compa(numb,numa):
    if numa==numb:
        return True
    else:
        return False
