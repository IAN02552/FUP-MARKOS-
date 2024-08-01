# Leia uma matriz 4 × 4 , conte e escreva quantos valores maiores que 10 ela possui.    
    
matriz = [] 
maior = 0
for c in range(4):  
    linha = []  
    for j in range(4):  
        n1 = int(input("")) 
        linha.append(n1)    
    matriz.append(linha)    
  
for c in range(4):  
    for j in range(4):  
        if matriz[c][j] > 10:   
            maior += 1  
print(maior) 
        