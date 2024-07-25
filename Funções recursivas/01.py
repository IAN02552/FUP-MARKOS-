#Crie uma função recursiva que receba um número inteiro positivo n e calcule o somatório dos números de 1 até n.    
def funcao(x):
    if x == 0:
        return x
    else:
        return x+funcao(x-1)