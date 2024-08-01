# Faça um programa que permita ao usuário entrar com uma matriz de 5 × 5 números reais. Em seguida, gere um vetor unidimensional contendo a soma dos números de cada coluna da matriz e mostre na tela esse vetor.  

l = []  
for c in range(5):  
    linha = []  
    for j in range(5):  
        linha.append(int(input("")))    
    l.append(linha) 

l1soma = [] 
for c in range(5):  
    soma = 0    
    for j in range(5):  
        soma += l[j][c] 
    l1soma.append(soma) 
print(l1soma)