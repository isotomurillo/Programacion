def list_op(lis):
    if isinstance (lis,list):
        return oper(lis,len(lis),1,0)
    else:
        return "Error"

def oper(lis,largo,res,indice):
    if indice==0:
        return  res
    else: return oper(lista,largo, res*lis[indice],indice+1)
