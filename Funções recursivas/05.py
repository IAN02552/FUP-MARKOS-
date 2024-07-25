# Faça uma função recursiva que receba um número inteiro positivo n e imprima todos os números naturais de 0 até n em ordem crescente.  
def funcao(n):  
    
    if n < 0:
        return
    funcao(n-1)
    print(n)