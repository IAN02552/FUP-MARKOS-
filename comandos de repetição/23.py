#Faça um programa para exibir a tabuada de 1 a 9 .  
cont = 1  
for c in range(9): 
    for j in range(10):  
        print(f"{cont} + {j} = {cont+j}")   
    cont += 1