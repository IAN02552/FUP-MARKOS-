#Faça um programa que simule uma calculadora com as 4 operações básicas. O usuário digita o primeiro número, escolhe a operação e em seguida digita o segundo número, exatamente nessa ordem. O programa deve mostrar o resultado da operação.  
n1 = float(input(""))   
op = str(input("")) 
n2 = float(input(""))   
if op == "+":   
    print(n1+n2)    
if op == "/":   
    print(f"{n1/n2:.2f}")    
if op == "-":   
    print(n1-n2)    
if op == "*":   
    print(f"{n1*n2:.2f}")