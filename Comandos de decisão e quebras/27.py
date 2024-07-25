#Escreva um algoritmo que leia um conjunto de n números e mostre qual foi o menor e o maior valor fornecido.  
n1 = int(input("")) 
menor = maior = None
for c in range(n1): 
    n2 = float(input(""))   
    if c == 0:  
        maior = menor = n2   
    if n2 > maior:  
        maior = n2
    if n2 < menor:  
        menor = n2
print(f"{menor:.2f}")   
print(f"{maior:.2f}")