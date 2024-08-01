# Leia uma matriz 4 × 4. Calcule a soma dos elementos que estão abaixo da diagonal principal. Não use comandos nem funções do python ou de suas bibliotecas que já façam isso.  

l = []  
for c in range(4):  
    linha = []  
    for j in range(4):  
        linha.append(int(input("")))    
    l.append(linha) 
soma = 0
for c in range(4):  
    for j in range(4):  
        if c > j:   
            soma += l[c][j]   
print(soma)