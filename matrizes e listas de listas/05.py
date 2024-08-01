# Leia uma matriz 5 × 5. Leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e, ao final, escrever a localização (linha e coluna) ou uma mensagem de "Nao encontrado".  

l = []  
for c in range(5):  
    linha = []  
    for j in range(5):  
        n1 = int(input("")) 
        linha.append(n1)    
    l.append(linha) 
num = int(input(""))    
col = lin = controle = -1   
for c in range(5):  
    for j in range(5):  
        if l[c][j] == num and controle == -1:  
            col = j
            lin = c 
            controle = 0
        
if col == -1 or lin == -1:    
    print("Nao encontrado") 
else:   
    print(lin)  
    print(col)
