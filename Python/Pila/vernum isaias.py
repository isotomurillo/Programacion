def vernum (lista,num):
    if type (lista)==list and type (num)==int:
        return vernum_aux(lista,num)
    else:
        return "Error"
def vernum_aux(lista,num):
    if lista ==[]:
        return []
    elif lista[0]== num:
        return vernum_aux(lista[1:],num)
    else: return [lista [0]]+vernum(lista [1:],num)
