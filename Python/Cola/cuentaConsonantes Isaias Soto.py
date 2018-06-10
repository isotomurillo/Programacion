def contarConsonantes (palabra):
    if isinstance (palabra,str):
        return cuenta(palabra,0)
    else:
        return "No es palabra"

def cuenta(palabra,cont):
    if palabra ==[]:
        return cont
    elif palabra[0]=='a'or'e'or'i'or'o'or'u':
        return cuenta(palabra[1:],cont)
    else:
        return cuenta(palabra[1:],cont+1)
