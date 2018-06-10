def transp (mat):
    if isinstance (mat,list):
        return trans (mat,0,0,len(mat),len(mat[0]),[])
    else:
        return "Error"

def trans (mat,col,fil,numf,numc,mat2):
    if fil==numf:
        return mat2
    elif col==numc:
        return trans(mat,fil+1,col,numf,numc,mat2)
    else:
        return trans(mat,fil,col,numf,numc,mat2+[mat[fil,col]])
