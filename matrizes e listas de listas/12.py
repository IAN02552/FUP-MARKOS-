 # Leia uma matriz 4 × 4. Calcule e imprima sua transposta. Não use comandos nem funções do python ou de suas bibliotecas que já façam isso.    

l = []  
for c in range(4):  
    linha = []  
    for j in range(4):  
        linha.append(int(input("")))    
    l.append(linha)

for c in range(4):  
    for j in range(4):  
        print(l[j][c],end = " ")    
    print()  
        