# Faça um programa que receba do usuário um vetor com 10 inteiros. Em seguida deverá ser mostrado na tela o maior e o menor valor desse vetor.  
l = []  
maior = menor = 0   
for c in range(10): 
    n1 = int(input("")) 
    l.append(n1)    
for c in range(len(l)): 
    if c == 0:  
        maior = menor = l[c]    
    elif l[c] > maior:    
        maior = l[c]    
    elif l[c] < menor:  
        menor = l[c]    
print(maior)    
print(menor)  
