# Escreva uma função recursiva que calcule a sequência dada por: F(1) = 1; F(2) = 2; e F(n) = 2*F(n − 1) + 3*F(n − 2).  
def funcao(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return 2*funcao(n - 1) + 3*funcao(n - 2)