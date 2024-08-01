# Faça um programa que preenche uma matriz de tamanho nxn com o produto do valor da linha e da coluna de cada elemento. Em seguida, imprima na tela a matriz, em forma de tabela.   

matriz = [] 
n = int(input(""))  
for c in range(n):  
    linha = []  
    for j in range(n):  
        linha.append(c*j)   
    matriz.append(linha)    
for c in range(n):  
    for j in range(n):  
        print(matriz[c][j], end = " ")  
    print()   
