#Faça uma função que receba um inteiro x e um inteiro não-negativo n e, usando laço de repetição, calcule x**n e retorne o resultado.   
def funcao(x, n):
    result = 1  
    for c in range(n):
        result *= x
    return result