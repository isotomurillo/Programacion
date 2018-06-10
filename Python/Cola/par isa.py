def Num_par(num): 

    if isinstance (num, int) and (num >0): 

        return Num_par_aux(num), Num_impar(num)

    else: 

        return 'Error' 
def Num_par_aux(num):
    if (num==0):
        return 0
    else:
        if ((num%10)%2)==0:
            return 1+Num_par_aux(num//10)
        else:
            return Num_par_aux(num//10)
        
def Num_impar(num):

    if (num==0):
        return 0
    else:
        if not((num%10)%2)==0:
            return 1+Num_impar(num//10)
        else:
            return Num_impar(num//10)
