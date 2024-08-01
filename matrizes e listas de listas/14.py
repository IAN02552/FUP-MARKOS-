# Faça um programa que leia duas matrizes A e B de tamanho 4 × 5 cada uma. Calcule a matriz   C = A + B. Não use comandos nem funções do python ou de suas bibliotecas que já façam isso.   

A = []  
for c in range(4):  
    linha = []  
    for j in range(5):  
        linha.append(int(input("")))    
    A.append(linha) 

B = []  
for c in range(4):  
    linha = []  
    for j in range(5):  
        linha.append(int(input("")))    
    B.append(linha) 

C = []  
for c in range(4):  
    linha = [] 
    for j in range(5):  
        linha.append(A[c][j]+B[c][j])   
    C.append(linha) 

for c in range(4):  
    for j in range(5):  
        print(C[c][j],end = " ")    
    print()
    
