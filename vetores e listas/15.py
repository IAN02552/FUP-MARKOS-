# Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais, se sim escreva esses valores na tela.    
l = []  
controle = []  
for c in range(10): 
    l.append(int(input("")))           
for c in range(len(l)): 
    for j in range(c+1,len(l)):   
        if l[c] == l[j]: 
            print(l[j])
