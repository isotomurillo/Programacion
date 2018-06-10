def ordenar (lis):
    if isinstance (lis,list):
        return orden(lis,0,0)
    else:
        return "Error"


def orden (lis,ind1,ind2):
    if ind2==len(lis)-1:
        return lis
    elif ind1==len(lis)-1:
        return orden(lis,0,ind2+1)
    elif lis[ind1]>lis[ind1+1]:
        aux=lis[ind1]
        lis[ind1]=lis[ind1+1]
        lis[ind1+1]=aux
        #lis[ind1],lis[ind1+1]=
        #   lis[ind1+1],lis[ind1]

    return orden(lis,ind1+1,ind2)
