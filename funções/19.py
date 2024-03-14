#Escreva uma função que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.   
def funcao(x):
    nota100 = x//100
    x = x%100
    nota50 = x//50
    x = x%50
    nota20 = x//20
    x = x%20
    nota10 = x//10
    x = x%10 
    nota5 = x//5
    x = x%5
    nota2 = x//2
    x = x%2
    nota1 = x
    return nota100,nota50,nota20,nota10,nota5,nota2,nota1   
x = int(input(""))
y1,y2,y3,y4,y5,y6,y7 = funcao(x)
print(f"{y1}")
print(f"{y2}")
print(f"{y3}")
print(f"{y4}")
print(f"{y5}")
print(f"{y6}")
print(f"{y7}")