# Leia uma matriz 4 × 4. Calcule a soma dos elementos que estão na diagonal secundária. Use apenas um comando de repetição. Não use comandos nem funções do python ou de suas bibliotecas que já façam isso.    

l = []  
for c in range(4):  
    linha = []  
    for j in range(4):  
        linha.append(int(input("")))    
    l.append(linha) 
     
diag = 3    
soma = 0
for c in range(4):  
    for j in range(4):  
        if j == diag:     
            diag -= 1   
            soma += l[c][j]  
print(soma)  
              