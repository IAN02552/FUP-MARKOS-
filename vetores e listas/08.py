# Leia um vetor com 15 posições. Somar e mostrar os números que são ímpares.    

l = []  
soma = 0
for c in range(15): 
    n1 = int(input("")) 
    if n1 % 2 == 1:
        soma += n1
    l.append(n1)
print(soma)
for c in range(len(l)): 
    if l[c] % 2 == 1:   
        print(l[c])

