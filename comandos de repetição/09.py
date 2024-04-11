#Faça uma função que calcule e retorne a soma dos N primeiros números pares (considere o 0 como o primeiro número par). 
    
def funcao(x):  
    soma = 0    
    par = 0 
    for c in range(1,x):  
        
        par += 2    
        soma = soma+par 
    return soma 
    
x = int(input(""))
y = funcao(x)
print(f"{y}")