#Faça uma função para verificar se um número é um quadrado perfeito. Ex: 1, 4, 9... 
def funcao(x):  
    if (x**(1/2))**2 == x:  
        return "True"  
    if (x**(1/2))**2 != x:   
        return "False"  
x = float(input(""))
y = funcao(x)
print(f"{y}")