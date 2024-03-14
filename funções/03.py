#Faça uma função que, a partir das medidas dos lados de um retângulo, calcule a área e o perímetro deste retângulo. 
def funcao(x1,x2):
    area = x1*x2
    perimetro = 2*(x1+x2)
    return area,perimetro   
x1 = float(input(""))
x2 = float(input(""))
y1, y2 = funcao(x1, x2)
print(f"{y1:.2f}")
print(f"{y2:.2f}")