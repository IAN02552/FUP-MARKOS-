# Crie um programa que lê 10 valores inteiros e, em seguida, mostre na tela os valores lidos # # na ordem inversa.  
l = []  
for c in range(10): 
    n1 = int(input("")) 
    l.append(n1)    

for c in range(len(l)-1,-1,-1):    
    print(l[c])