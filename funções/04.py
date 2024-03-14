#Faça uma função que, dado um número inteiro e retorne o seu antecessor e o seu sucessor.   
def funcao(x):
    antecessor = x-1
    sucessor = x+1
    return antecessor, sucessor 
x = int(input(""))
y1,y2 = funcao(x)
print(f"{y1}")
print(f"{y2}")