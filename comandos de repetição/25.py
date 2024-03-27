#Faça uma função que receba um inteiro n como parâmetro, calcule e retorne o resultado da seguinte série: S = 2/4 + 5/5 + 10/6 + … + (n2 + 1)/(n + 3)   
def funcao(x):
    s = 0
    for c in range(1,x+1):
        s = s+(c**2+1)/(c+3)
    return s