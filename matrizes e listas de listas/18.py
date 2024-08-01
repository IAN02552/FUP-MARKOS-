# Gere uma matriz 5 × 5 com inteiros aleatórios no intervalo [1, 20], encontrados a partir de uma semente dada como entrada. Escreva um programa que transforme a matriz gerada numa matriz triangular inferior, ou seja, atribuindo zero a todos os elementos acima da diagonal principal. Imprima a matriz original e a matriz transformada. Não use nenhum comando de decisão (se/então/senão).  

import random   
l = []  
n1 = int(input("")) 
random.seed(n1)     
for i in range(5):  
    linha = []  
    for j in range(5):  
        linha.append(random.randint(1,20))  
    l.append(linha) 

for i in range(5):  
    for j in range(5):  
        print(l[i][j], end = " ")   
    print()
print() 
incio = 1   
fim = 5
for i in range(5):  
    for j in range(incio):  
        print(l[i][j],end = " ")    
    for k in range(fim-incio):  
        print(0,end = " ")  
    incio += 1 
    print()

