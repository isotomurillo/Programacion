def nummen (lista):  

    if type (lista)==list:  

        return nummen_aux(lista), nummax(lista)  

    else:  

        return "Error" 

def nummen_aux (lista): 

    if len(lista)==1:#lista==[lista[0]]: 

        return lista[0] 

    elif lista[0]<=lista[1]: 

       return nummen_aux (lista[2:]+[lista[0]]) 

    else: 

        return nummen_aux(lista[1:])
    
def nummax (lista): 

    if len(lista)==1:#lista==[lista[0]]: 

        return lista[0] 

    elif lista[0]>=lista[1]: 

       return nummax (lista[2:]+[lista[0]]) 

    else: 

        return nummax(lista[1:])
