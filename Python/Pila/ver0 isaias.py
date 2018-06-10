def ver0 (lista):
    if type (lista)==list:
        return ver0_aux(lista)
    else:
        return "Error"

def ver0_aux(lista):
    if lista== []:
        return False
    elif lista[0]==0:
        return True
    else:
        return ver0_aux(lista[1:])
        
