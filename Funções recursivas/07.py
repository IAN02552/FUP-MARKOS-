# Faça uma função recursiva que receba um número inteiro positivo par n e imprima todos os números pares de 0 até n em ordem crescente. 
def funcao(x):
    if x < 0:
        return 
    funcao(x-1)
    if x%2 == 0:
        print(x)