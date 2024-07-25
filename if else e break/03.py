#Ler 4 números inteiros e calcular a soma dos que forem par.    
soma = 0    
for c in range(4):  
    n1 = int(input("")) 
    if n1%2 == 0:   
        soma = soma+n1  
print(soma)   
