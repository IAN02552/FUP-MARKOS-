#Faça uma função que receba um valor inteiro n ≥ 0 e calcule o seu fatorial n!. Lembrete: 0!=1.   
def funcao(x):
    fatorial = 1
    for c in range(1,x+1):
        fatorial = fatorial*c
    return fatorial 