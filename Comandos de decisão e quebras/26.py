#Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido. 
c = 0   
maior = menor = 0   
while c != 10:  
    n1 = int(input("")) 
    if c == 0:  
        maior = menor = n1
    if n1 > maior:  
        maior = n1  
    if n1 < menor:  
        menor = n1  
    c += 1  
print(f"{menor:.2f}")    
print(f"{maior:.2f}")