# Escreva uma função recursiva que calcule a soma dos primeiros n cubos:     
# S(n) = 13 + 23 +...+n3.  
def funcao(x):
    if x == 1:
        return x
    else:
        return x**3+funcao(x-1)
