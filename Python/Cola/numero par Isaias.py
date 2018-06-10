def numeros_primos(num):
    if isinstance (num, int): 
        return numero_primo_aux(abs(num))
    else: 
        return 'Error' 




def numero_primo_aux(num):
    if num==0 or num==1 or num==(-1):
        return "Numero Especial"
    elif num>1:
        return 1
    else:
        return 2
        
