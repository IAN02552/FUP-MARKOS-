#Faça um função para verificar se um número é positivo ou negativo. Sendo que o valor de retorno será 1 se positivo, −1 se negativo e 0 se for igual a zero.    
def funcao(x):  
    if x > 0:   
        return 1    
    if x == 0:  
        return 0    
    if x < 0:   
        return -1   
x = float(input(""))
y = funcao(x)
print(f"{y}")