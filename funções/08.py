#Faça uma função que converta a temperatura de graus Celsius para Fahrenheit. Fórmula: F = C * (9.0/5.0) +  
def funcao(x):
    fahrenheit = x*(9.0/5.0)+32
    return fahrenheit   
x = float(input(""))
y = funcao(x)
print(f"{y:.2f}")