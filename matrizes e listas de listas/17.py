# Faça um programa que carregue uma matriz 12 × 13 e divida todos os elementos de cada coluna # pelo maior elemento daquela coluna que seja primo. Caso a coluna não possua um número primo, # divida a coluna pelo menor número da coluna. Escreva a matriz original e a modificada.
    
def primo(a):   
    a = abs(a)
    div = 0 
    if a == 1 or a == -1:   
        return True
    if a < 0:   
        for c in range(1,a*-1+1):   
             if a%c == 0:
                div += 1
        if div == 2:
            return True
        else:
            return False
    if a == 0:  
        return False    

    for c in range(1,a+1):
        if a%c == 0:
            div += 1
    if div == 2:
        return True
    else:
        return False

ma_ori = []

for i in range(12): 
    linha = []  
    for j in range(13): 
        linha.append(int(input("")))    
    ma_ori.append(linha)
# imprime a matriz original
for i in range(12): 
    for j in range(13): 
        print(f"{ma_ori[i][j]:.2f}",end = " ")  
    print() 
print()
# ciando a matriz modificada 
ma_mod = [] 
for i in range(13): 
    linha = []  
    maior_primo = 0
    menor = 0
    for j in range(12): 
        maior = primo(ma_ori[j][i]) 
        if j == 0:  
            menor = ma_ori[j][i] 
        if j == 0 and ma_ori[j][i] < 0:    
            menor = ma_ori[j][i]*-1   
        if ma_ori[j][i] < menor:   
            menor = ma_ori[j][i]
        if maior == True and ma_ori[j][i] > maior_primo:   
            maior_primo = ma_ori[j][i] 
    if maior_primo != 0:    
        for k in range(12): 
            linha.append(ma_ori[k][i]/maior_primo) 
    if maior_primo == 0:   
        for k in range(12): 
            linha.append(ma_ori[k][i]/menor) 
    ma_mod.append(linha)    
# imprimir a matriz modificada    
for i in range(12): 
    for j in range(13): 
        print(f"{ma_mod[j][i]:.2f}",end = " ")  
    print()

            
