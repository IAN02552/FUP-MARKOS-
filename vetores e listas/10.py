# Leia um vetor de 20 inteiros e atribua 0 para todos os elementos que possuírem valores negativos. 
l = []  
for c in range(20): 
    n1 = int(input("")) 
    l.append(n1)    
for c in range(len(l)): 
    if l[c] < 0:    
        l[c] = 0    
    print(l[c])