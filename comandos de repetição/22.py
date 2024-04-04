#Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado triangulo de Floyd. Para n = 6, temos:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21 
n1 = int(input("")) 
num = 1
for c in range(1,n1+1): 
    for j in range(1,c+1):  
        print(f"{num}",end = " ")   
        num += 1   
    print()
