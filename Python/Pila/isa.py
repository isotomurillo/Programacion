def numveces(num): 

    if isinstance (num, int) and (num >0): 

        return numveces_aux(abs(num)) 

    else: 

        return 'Error' 

  

def numveces_aux (num):
    digito=input("introduce numero")

    if (num%10)== digito:
        1+numveces_aux(num)
    else:
        numvecesaux(num)
