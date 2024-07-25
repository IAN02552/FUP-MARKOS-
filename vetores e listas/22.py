# Faça um programa que preencha um vetor de tamanho 100, com os 100 primeiros naturais que não são múltiplos de 7 ou que terminam com 7.    

l = []  
c = 1 
while True: 
    if len(l) == 100:   
        break 
    if c%10 != 7 and c%7 != 0:  
        l.append(c)  
    c += 1  
print(l)    
