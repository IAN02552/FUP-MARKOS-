# Leia um número n e crie uma matriz n×n. Preencha com 1 a diagonal principal e com 0 os demais elementos. Escreva ao final a matriz obtida. Use comandos de repetição. 

matriz = [] 
n = int(input(""))   
for c in range(n):  
    linha = []  
    for j in range(n):  
        if c == j:  
            linha.append(1) 
        else:   
            linha.append(0) 
    matriz.append(linha)    
for c in range(n):  
    for j in range(n):  
        print(matriz[c][j], end = " ")  
    print()