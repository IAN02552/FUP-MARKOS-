#Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido. 
n1 = float(input(''))
n2 = float(input(''))
n3 = float(input(''))
n4 = float(input(''))
n5 = n1+n2+n3
print(f"{n4*(n1/n5):.2f}")
print(f"{n4*(n2/n5):.2f}")
print(f"{n4*(n3/n5):.2f}")