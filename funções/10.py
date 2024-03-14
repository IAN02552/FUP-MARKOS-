#Crie uma função que, dado um ângulo em graus, retorne-o convertido em radianos. A fórmula de conversão é: R = G * π/180 , sendo G o ângulo em graus e R em radianos.   
def funcao(x):
    radianos = (x*3.141592653)/180
    return radianos 
x = float(input(""))
y = funcao(x)
print(f"{y:.2f}") 