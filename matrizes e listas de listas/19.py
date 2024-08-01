# Faça um programa que gere uma matriz m × n de inteiros aleatórios (gerados a partir de uma semente), calcule e mostre a média dos elementos das linhas pares da matriz e a quantidade de números negativos e divisíveis por 3 das linhas ímpares da matriz. A quantidade de linhas m, a quantidade de colunas n, a semente dos números aleatórios e o intervalo de geração serão dados como entrada para o programa.  
    
import random   
l = []
m = int(input(""))  
n = int(input(""))  
semente = int(input("")) 
random.seed(semente)    
inicio = int(input("")) 
fim = int(input(""))    
for i in range(m):  
    linha = []  
    for j in range(n):  
        linha.append(random.randint(inicio,fim))    
    l.append(linha) 

for i in range(m):   
    for j in range(n):  
        print(l[i][j], end = " ")         
    print() 
linha_par = 0   
contador = 0    
cont_impar = 0 

for i in range(m):  
    linha_par = 0   
    contador = 0    
    cont_impar = 0  
    for j in range(n):  
        if i%2 == 0:    
            linha_par += l[i][j]    
            contador += 1   
        if i%2 == 1 and l[i][j] < 0 and l[i][j]%3 == 0:    
            cont_impar += 1  
    if contador != 0:   
        print(f"{linha_par/contador:.2f}")   
    if i%2 == 1:   
        print(f"{cont_impar}")
    
 
    