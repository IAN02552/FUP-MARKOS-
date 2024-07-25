#Leia um valor inteiro positivo em segundos, e imprima-o em horas, minutos e segundos.  
n1 = int(input(''))
n2 = n1//3600
n3 = (n1%3600)//60
n4 = (n1%3600)%60
print(n2)
print(n3)
print(n4)