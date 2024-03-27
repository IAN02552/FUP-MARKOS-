#Ler três valores e determinar o maior entre eles.  
maior = 0   
for c in range(3):  
    n1 = float(input("")) 
    if c == 0:  
        maior = n1  
    if n1 > maior:  
        maior = n1
print(maior)