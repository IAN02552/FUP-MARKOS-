#Faça uma função que, dado um valor N inteiro e positivo, calcule o valor de E, conforme a fórmula a seguir: E = 1 + 1/1! + 1/2! + 1/3! . . . 1/n!. 
def funcao(n):
    hn = 1  
    fatorial = 1  
    for i in range(1, n + 1):
        fatorial *= i  
        hn += 1 / fatorial  
    return hn