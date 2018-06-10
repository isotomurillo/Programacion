def ver (num,lis):
    if isinstance (lis,list):
        return Ver(num,lis)
    else:
        return "Error"

def Ver(num,lis):
    if lis==[]:
        return False
    elif num==lis[0]:
        return True
    else:
        return Ver(num,lis[1:])
