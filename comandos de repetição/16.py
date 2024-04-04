#Faça um programa que calcule e escreva o valor de S = 1/1 + 3/2 + 5/3 + 7/4 + … + 99/50.   
s = 1   
cont = 2
for c in range(3,100,2):   
    s = s+c/cont
    cont += 1   
print(f"{s:.10f}")