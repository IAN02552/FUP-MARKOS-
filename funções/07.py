#Faça uma função que, dado um número real, e retorne o resultado do quadrado desse número.  
def funcao(x):
    quadrado = x**2
    return quadrado     
x = float(input(""))
y = funcao(x)
print(f"{y:.2f}")