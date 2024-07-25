# Faça uma função recursiva que receba um número inteiro positivo n e imprima todos os números naturais de 0 até n em ordem decrescente.    
def funcao(n):
    if n < 0:
        return
    print(n)
    funcao(n-1)
 