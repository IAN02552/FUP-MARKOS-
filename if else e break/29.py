# Faça um programa que receba um valor inteiro n ≥ 0 e imprima se esse número é primo ou não.   
n1 = int(input("")) 
div = 0 
for c in range(1,n1+1): 
    if n1%c == 0:   
        div += 1    
if div == 2:    
    print("Primo")  
else:   
    print("Nao primo")