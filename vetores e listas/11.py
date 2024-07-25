# Faça um programa para ler a nota de 15 alunos e armazene em um vetor, calcule e imprima a média geral.    
    
l = []  
media = 0  
for c in range(15): 
    n1 = float(input(""))   
    l.append(n1)    
    media += n1
print(f"{media/15:.2f}")
