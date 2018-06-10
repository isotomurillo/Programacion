def numm (num): 

  if isinstance (num,int) and (num>0): 

    return numm_aux (num) 

  else: 

    return "Error" 

  

def numm_aux (num): 

  if num==0: 

    return 0 

  else: 

    return (num+5*((num*num)**2))+numm_aux(num-1) 
