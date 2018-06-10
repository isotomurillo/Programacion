def maymen(lis):
    if isinstance (lis,list):
        return mas(lis,lis[0]), men(lis,lis[0])
    else:
        return "Error"

def mas(lis,res):
    if lis==[]:
        return res
    elif lis[0]>res:
        return mas(lis[1:],lis[0])
    else:
        return mas(lis[1:],res)

def men(lis,res):
    if lis==[]:
        return res
    elif lis[0]<res:
        return men(lis[1:],lis[0])
    else:
        return men(lis[1:],res)
