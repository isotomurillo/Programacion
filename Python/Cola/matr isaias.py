class matr:
    def _init_(self):
        pass
    
    def llenado_matriz(self,num):
        if isinstance (num,int):
            return self.matt(num,0,0,[],[])
        else: return "Error"

    def matt(self,num,col,fil,film,mat):
        if fil==num:
            return mat
        elif col==num:
            return self.matt(num,0,fil+1,[],mat+[film])
        elif col==0 or col==num-1:
            return self.matt(num,col+1,fil,film+["*"],mat)
        elif fil==0 or col==num-1:
            return self.matt(num,col+1,fil,film+["*"],mat)
        else: return self.matt(num,col+1,fil,film+[0],mat)
