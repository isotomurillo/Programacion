def rotar(mat):
    if isinstance (mat,list):
        return rota(mat,0,0,[],[],0)
    else: return "Error"

def rota(mat,col,fila,listfil,mat2,fil):
    if col==len(mat):
        return mat2
    elif fila==len(mat[0]):
        return rota(mat,col+1,fila,listfil,mat2)
    elif len(listfil)<len(mat[0]):
        return rota(mat,col+1,fil,listfil+mat[fil][-1],mat2)
    elif len(listfil)==len(mat[0]):
        return rota(mat,0,0,[],mat2+listfil,fil+1)
    else:
        return rota (mat,col,fila+1,listfil,mat2,fil)
