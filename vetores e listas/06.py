# Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois valores X e Y quaisquer correspondente a duas posições no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados nas respectivas posições X e Y 
l = []  
for c in range(8):  
    n1 = float(input(""))   
    l.append(n1)    
x = int(input(""))  
y = int(input(""))  
print(f"{l[x]+l[y]:.2f}")