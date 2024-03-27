#Faça uma função que, dado número N, some todos os números inteiros de 1 a N, e retorne o resultado obtido. 
def funcao(x):  
    soma = 0    
    for c in range(1,x+1):  
        soma = soma+c   
    return soma 
x = int(input(""))
y = funcao(x)
print(f"{y}")