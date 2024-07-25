#Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999). Gere outro número formado pelos dígitos invertidos do número lido. Exemplo: Número Lido = 123, Número Gerado = 321. 
n1 = int(input(''))
n2 = n1%10
n3 = (n1//10)%10
n4 = n1//100
n5 = n2*100+n3*10+n4
print(n5)