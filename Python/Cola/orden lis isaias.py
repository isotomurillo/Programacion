def orden (lis):
    if isinstance (lis,list):
        return orden_aux(lis,0,len(lis))
    else:
        return "Error"

def orden_aux(lis,ind,lar):
    if ind>=lar:
        return []
    elif lis[0]>lis[1]:
        return [lis[ind+1],lis[ind]]+orden_aux(lis,ind+2,lar)
    else:
        return [lis[ind],lis[ind+1]]+orden_aux(lis,ind+2,lar)
        
