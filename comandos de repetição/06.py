#Faça um algoritmo que leia um número N, some todos os números inteiros de 1 a N, e mostre o resultado obtido.  
n1 = int(input("")) 
soma = 0
for c in range(1,n1+1): 
    soma = soma+c   
print(soma)