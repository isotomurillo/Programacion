def nummas (lis):
    if isinstance (lis,list):
        return mas(lis,1,len(lis),0), "menor" menos(lis,1,len(lis),0)
    else :"Error"

def mas(lis,indice,largo,res):
    if indice==largo:
        return res
    elif lis[indice-1]<=lis[largo-1]:
        return mas(lis,indice+1,largo,lis[indice])
    else:
        return mas(lis,indice,largo-1,lis[indice-1])

def menos(lis,indice,largo,res):
    if indice==largo:
        return res
    elif lis[indice-1]<=lis[largo-1]:
        return menos(lis,indice,largo-1,lis[indice-1])
    else:
        return menos(lis,indice+1,largo,lis[indice])
