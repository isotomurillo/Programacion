class  fig:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def getX(self):
        return self.__x

    def setX (sel,x):
        if x >=0 and x<=1023:
            self.__x=x
        else: print ("El valor debe estar entre 0 y 1023")
    def getY(self):
        return self.__y
    def setY(self):
        if y>=0 and y<=768:
            self.__y=y
        else: print ("El valor de y debe estar entre 0 y 768")
