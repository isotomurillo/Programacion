def multi(num):
    if isinstance (num,list):
        return multi_aux(num,1)
    else:
        return "Error"

def multi_aux(num,res):
    if num==[]:
        return res
    else:
        return multi_aux(num[1:],res*num[0])
