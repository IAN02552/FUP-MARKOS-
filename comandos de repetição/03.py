#Faça um programa que peça ao usuário para digitar 10 valores e mostre a soma deles.    
soma = 0  
for c in range(10): 
    n1 = float(input("")) 
    soma = soma+n1  
print(f"{soma:.2f}")