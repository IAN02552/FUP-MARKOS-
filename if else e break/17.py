#Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva, para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero   
c = 0   
while c == 0:   
    n1 = float(input(""))   
    if n1 <= 0: 
        break   
    else:   
        print(f"{n1**2:.2f}")    
        print(f"{n1**3:.2f}")    
        print(f"{n1**(1/2):.2f}") 