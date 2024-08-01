# Leia duas matrizes 4 × 4 e escreva uma terceira matriz com os maiores valores de cada posição das matrizes lidas. 

l1 = [] 
l2 = [] 
l3 = [] 

for c in range(4):  
    linha = []  
    for j in range(4):  
        linha.append(int(input("")))    
    l1.append(linha)    
for c in range(4):  
    linha = []  
    for j in range(4):  
        linha.append(int(input("")))    
    l2.append(linha)    

for c in range(4):  
    linha = []    
    for j in range(4):  
        maior = l1[c][j]    
        if l2[c][j] > maior:    
            maior = l2[c][j]    
        linha.append(maior) 
    l3.append(linha)    
        
for c in range(4):  
    for j in range(4):  
        print(l3[c][j],end = " ")   
    print()    
        
     
