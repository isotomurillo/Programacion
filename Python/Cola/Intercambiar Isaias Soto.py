def intercambiar(Lista):
    if isinstance (Lista,list):
        return cambio(Lista)
    else:
        return "No es na ista"

def cambio(Lista):
    if Lista==[]:
        return Lista
    else:
        return Lista[1]+Lista[0]+cambio(Lista[2:])
