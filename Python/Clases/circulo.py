
import math
from figini import fig
class circulo(fig):
    def __init__(self,x,y,r):
        super().__init__(x,y)
        self.__radio=r

    def getRadio(self,r):
        self.__radio=r

    def setRadio (self,r):
        self.__radio=r
    def calcularArea (self):
        return math.pi*(self.__radio**2)
