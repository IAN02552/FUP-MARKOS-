# Leia um vetor com 15 posições. Contar e escrever os valores pares desse vetor.    
l = []
l1 = []  
cont = 0  
for c in range(15): 
    n1 = int(input("")) 
    l.append(n1)    
for c in range(len(l)): 
    if l[c]%2 == 0: 
        cont += 1   
        l1.append(l[c]) 
print(cont) 
for c in range(len(l1)):    
    print(l1[c])