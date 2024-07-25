# Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprimir todos os conjuntos.  
l = []  
for c in range(10): 
    n1 = float(input("")) 
    l.append(n1)    
l1 = l    
for c in range(len(l1)): 
    print(f"{l1[c]:.2f}")   
for c in range(len(l1)):    
    print(f"{l1[c]**2:.2f}")