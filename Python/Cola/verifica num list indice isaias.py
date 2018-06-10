def ver (num,lis):
    if  isinstance (lis,list):
        return Ver(num,lis,0,len(lis))
    else:
        return "Error"

def Ver(num,lis,ind,lar):
    if ind==lar:
        return False
    elif num==lis[ind]:
        return True
    else:
        return Ver(num,lis,ind+1,lar)
