#Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média. 
soma = 0    
c = 0 
while c != 10: 
    n1 = int(input())   
    if n1 > 0:  
        soma += n1  
        c += 1
print(soma/10)