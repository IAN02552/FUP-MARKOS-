#Elabore um programa que faça leitura de vários números inteiros, até que se digite um número negativo. O programa tem que retornar o maior e o menor número lido.    
c = 0   
n1 = 1  
maior = menor = None    
   
while n1 > 0:   
    n1 = int(input(""))
    if n1 < 0:  
        break  
    if c == 0:  
        maior = menor = n1  
        c += 1   
    if n1 > maior:  
        maior = n1
    if n1 < menor:  
        menor = n1  
if maior != None and menor != None:  
    print(maior)    
    print(menor)