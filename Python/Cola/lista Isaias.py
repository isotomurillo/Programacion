def lispar(lis):
    if isinstance (lis,list):
        return par(lis,len(lis),0,[])
    else:
        return "Error"

def par (lis,largo,indice,lis2):
    if indice==largo:
        return lis2
    elif lis[0]%2==0:
        return par(lis[1:],largo,indice+1,lis2+[lis[0]])
    else:
        return par(lis[1:],largo,indice+1,lis2)
