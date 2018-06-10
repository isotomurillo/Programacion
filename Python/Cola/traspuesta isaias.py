def tras (mat):
    return trasp(mat,0,0,[],[])

def trasp (mat,fil,col,film,tras):
    if col==len(mat[0]):
        return tras
    elif fil==len(mat):
        return (trasp(mat,0,col+1,[],tras+[film]))
    else: return trasp(mat,fil+1,col,film+[mat[fil][col]],tras)
