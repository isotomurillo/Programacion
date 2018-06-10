def consecutivos (mat):
    if isinstance (mat,list):
        return array(mat,0,0,1,len(mat))
    else:
        return "Error"

def array(mat,colum,fila,num,largo):
    if num>largo**2: return True
    elif fila==largo:
        return False
    elif colum==largo:
        return array(mat,0,fila+1,num,largo)
    elif num==mat[fila][colum]:
        return array(mat,0,0,num+1,largo)
    else:
        return array(mat,colum+1,fila,num,largo)
