# Crie uma função recursiva que receba dois inteiros positivos n e k e calcule n**k.    
def funcao(x1,x2):
   
    if x1 == 0 or x2 == 0:
        return 1 
    else:
        return x1*funcao(x1,x2-1)