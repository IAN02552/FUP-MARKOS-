# Leia 10 números inteiros e armazene em um vetor. Em seguida escreva os elementos que são  primos e suas respectivas posições no vetor. 

l = []  
for c in range(10): 
    n1 = int(input("")) 
    l.append(n1)    
     
for c in range(len(l)): 
    div = 0 
    co = l[c]    
    if l[c] < 0:    
        co = l[c]*-1    
    
    for j in range(1,co+1):    
        if l[c]%j == 0:    
            div += 1    
    if div == 2:    
        print(l[c]) 
        print(c)
