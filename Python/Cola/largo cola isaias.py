def dvi3(num):
    if isinstance (num,int):
        return div3_aux(num,0,0)
    else:
        return "Error: el numero no es entero"

def div3_aux(num,res,po):
    if (num==0):
        return res
    elif ((num%10)%3)==0:
        return div3_aux(num//10,res,po)
    else:
        return div3_aux(num//10,res+(num%10)*(10**po),po+1)
    

        
