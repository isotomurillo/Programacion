def sumalistapar (lista): 

    if type(lista)==list: 

        return sumalistapar_aux(lista),sumalistaimpar_aux(lista) 

    else: return "error" 

  

def sumalistaimpar_aux(lista): 

    if lista == []: 

        return 0 

    elif lista [0]%2==1: 

        return lista[0]+sumalistaimpar_aux(lista[1:]) 

    else: 

        return sumalistaimpar_aux(lista[1:]) 

def sumalistapar_aux(lista): 

    if lista == []: 

        return 0 

    elif lista [0]%2==0: 

        return lista[0]+sumalistapar_aux(lista[1:]) 

    else: 

        return sumalistapar_aux(lista[1:]) 
