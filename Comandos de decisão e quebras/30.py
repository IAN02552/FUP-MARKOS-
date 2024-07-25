# Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número foi lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário. 
n1 = int(input("")) 
maior = quant = None
for c in range(n1): 
    n2 = int(input("")) 
    if c == 0:  
        maior = n2  
        quant = 1      
    if n2 > maior:  
        maior = n2
        quant = 1   
    if n2 == maior: 
        quant += 1   
print(maior)    
print(quant-1)  
