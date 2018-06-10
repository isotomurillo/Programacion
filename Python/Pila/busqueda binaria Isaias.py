def bus_bin (num,lis):
    if isinstance (num,int) and isinstance (lis,list):
        return bus(num,lis,(len(lis)-1)//2,2,len(lis)-1)
    else :
        return "Error"

def bus(num,lis,ind1,ind2,lar):
    if ind2>lar or ind1==lar or ind2==0:
        return False
    elif lis[ind1]>num:
        return bus(num,lis,ind1-(lar//ind2),ind2-1,lar)
    elif lis[ind1]==num:
        return True
    else:
        return bus(num,lis,ind1+(lar//ind2),ind2+2,lar)
