#Elaborar um programa para calcular e imprimir o volume (V) de uma esfera e a área (A) de sua superfície, dado o valor de seu raio (R). A fórmula do volume da esfera é V = 4/3 πR3 e A = 4πR2 .
n1 = float(input(''))
print(f"{4/3*3.14159265*(n1**3):.2f}")
print(f"{4*3.14159265*(n1**2):.2f}")