# Faça um programa que leia um vetor de 100 posições para números reais e, depois, um código inteiro. Se o código for 0, finalize o programa; se o código for 1, mostre o vetor na ordem direta; se for 2, mostre o vetor na ordem inversa. Caso, o código seja diferente de 1 e 2 escreva uma mensagem informando que o código é inválido. O programa sempre deve pedir outro código, e terminar somente quando o código for 0.    
    
l = []  
for c in range(100):    
    n1 = float(input(""))   
    l.append(n1)       
while True: 
    op = int(input(""))  
    if op == 0: 
        break  
    elif op == 1: 
        for c in range(len(l)): 
            print(l[c]) 
    elif op == 2:   
   
        for j in range(len(l)+1): 
            if j != 0:   
                print(l[-j]) 
    else:   
        print("Codigo invalido")    
   
    