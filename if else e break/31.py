#Faça um programa que receba dois números. Calcule e mostre:
# A soma dos números pares desse intervalo de números (intervalo incluindo os números dados);
# A multiplicação dos números ímpares desse intervalo (intervalo incluindo os números dados);   
n1 = int(input("")) 
n2 = int(input("")) 
maior = menor = 0   
if n1 > n2: 
    maior = n1  
    menor = n2  
else:   
    maior = n2
    menor = n1  
soma = 0    
mul = 1
for c in range(menor,maior+1):    
    if c%2 == 0:    
        soma += c   
    if c%2 == 1:    
        mul *= c    
print(soma) 
print(mul)