#Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com exceção dele próprio. Exemplo: a soma dos divisores de 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78. 
n1 = int(input("")) 
soma = 0
for c in range(1,n1): 
    if n1%c == 0:   
        soma = soma+c
print(soma)