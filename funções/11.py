#Crie uma função que, dados três valores, retorne a soma dos quadrados dos três valores e o quadrado da soma dos três valores.  
def funcao(x1,x2,x3):
    x4 = x1**2+x2**2+x3**2
    x5 = (x1+x2+x3)**2
    return x4,x5    
x1 = float(input(""))
x2 = float(input(""))
x3 = float(input(""))
y1,y2 = funcao(x1, x2, x3)
print(f"{y1:.2f}")
print(f"{y2:.2f}")