#Escreva uma função que, dadas as coordenadas x e y de pontos no R2 e retorne sua distância para a origem (0, 0).   
def funcao(x1,x2):
    y1 = ((x1**2)+(x2**2))**(1/2)
    return y1   
x1 = float(input(""))
x2 = float(input(""))
y = funcao(x1,x2)
print(f"{y:.2f}")