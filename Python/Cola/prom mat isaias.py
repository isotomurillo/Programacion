def suma_mat (mat):
    if isinstance (mat,list):
        return suma(mat,len(mat),len(mat[0]),0,0,0,0)
    else:
        return "Error"


def suma(mat,numf,numc,fil,col,res,cant):
    if fil==numf:
        return res//cant
    elif col==numc:
        return suma(mat,numf,numc,fil+1,0,res,cant)
    else:
        return suma(mat,numf,numc,fil,col+1,res+mat[fil][col],cant+1)
