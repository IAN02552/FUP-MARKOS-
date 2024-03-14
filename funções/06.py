#Elabore uma função para calcular o volume (V) de uma esfera e a área (A) de sua superfície, dado o valor de seu raio (R). A fórmula do volume da esfera é V = 4/3 πR3 e A = 4πR2 . 
def funcao(x):
    volume = (4/3)*3.141592653*(x**3)
    area = 4*3.141592653*(x**2)
    return volume, area     
x = float(input(""))
y1,y2 = funcao(x)
print(f"{y1:.2f}")
print(f"{y2:.2f}")