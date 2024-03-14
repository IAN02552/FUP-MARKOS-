#Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada deu para a realização da aposta. Faça uma função que receba quanto cada apostador investiu e o valor do prêmio, e retorne quanto cada um ganharia do prêmio com base no valor investido. 
def funcao(x1,x2,x3,x4):
    y = x1+x2+x3
    y1 = x4*(x1/y)
    y2 = x4*(x2/y)
    y3 = x4*(x3/y)
    return y1,y2,y3 
x1 = float(input(""))
x2 = float(input(""))
x3 = float(input(""))
x4 = float(input(""))
y1,y2,y3 = funcao(x1,x2,x3,x4)
print(f"{y1:.2f}")
print(f"{y2:.2f}")
print(f"{y3:.2f}")