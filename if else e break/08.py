# Faça um programa que receba dois números e execute as operações listadas a seguir de acordo com a escolha do usuário:
# 1: Média entre os números digitados
# 2: Diferença do maior pelo menor
# 3: Produto entre os números digitados
# 4: Divisão do primeiro pelo segundo
# Se a opção digitada for inválida, mostrar uma mensagem de erro e terminar a execução do programa. Dica do Brother: Na operação 4 o segundo número deve ser diferente de 0.    
n1 = float(input("")) 
n2 = float(input("")) 
op = int(input("")) 
if op == 1: 
    print(f"{(n1+n2)/2:.2f}")    
elif op == 2: 
    maior = n1  
    menor = n1
    if n2 > maior:  
        maior = n2 
    if n2 < menor:  
        menor = n2  
    print(f"{maior-menor:.2f}")  
elif op == 3: 
    print(f"{n1*n2:.2f}")    
elif op == 4: 
    if n2 == 0: 
        print("Erro")   
    else:   
        print(f"{n1/n2:.2f}")    
else:   
    print("Erro")