#Faça uma função que receba um valor inteiro positivo em segundos, e retorne-o em horas, minutos e segundos.    
def funcao(x):
    horas = x//3600
    minutos = (x%3600)//60
    segundos = (x%3600)%60
    return horas,minutos,segundos   
x = int(input(""))
y1,y2,y3 = funcao(x)
print(f"{y1}")
print(f"{y2}")
print(f"{y3}")