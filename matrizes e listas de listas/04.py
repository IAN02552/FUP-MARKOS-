# Leia uma matriz 4 × 4, imprima a matriz e retorne a localização (linha e coluna) do maior valor.  

matriz = [] 
for c in range(4):  
    linha = [] 
    for j in range(4):  
        n1 = int(input("")) 
        linha.append(n1)    
    matriz.append(linha)    

maior = mlin = mcol = 0 
for c in range(4):  
    if c == 0:  
        maior = matriz[c][0]    
    for j in range(4):  
        if matriz[c][j] > maior:    
            maior = matriz[c][j]    
            mlin = c    
            mcol = j    
        print(f"{matriz[c][j]}", end = " ")    
    print() 
print(mlin) 
print(mcol) 
print(maior)
        