#Faça uma função que receba um número inteiro positivo P e retorne a soma dos algarismos de P! . Exemplo: Se P = 4 , P! = 24 . Logo, a soma de seus algarismos é 2 + 4 = 6. 
def funcao(x):  
    fatorial = 1
    soma = 0
    for c in range(1,x+1):
        fatorial = fatorial*c   
    while fatorial >= 10: 
        soma = soma+(fatorial%10)
        fatorial = fatorial//10
    return soma+fatorial    
x = int(input(""))
y = funcao(x)
print(f"{y}")