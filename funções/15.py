#Faça uma função que receba um número inteiro de 4 dígitos (de 1000 a 9999) e retorne os 4 dígitos separados, cada um em uma variável diferente.    
def funcao(x):
    y1 = x//1000
    y2 = (x//100)%10
    y3 = (x//10)%10
    y4 = x%10
    return y1,y2,y3,y4  
x = int(input(""))
y1,y2,y3,y4 = funcao(x)
print(f"{y1:0}")
print(f"{y2:0}")
print(f"{y3:0}")
print(f"{y4:0}")