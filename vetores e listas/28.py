# Faça um programa para ler 12 inteiros DIFERENTES a serem armazenados em um vetor. Os dados deverão ser armazenados na ordem que forem sendo lidos, mas caso o usuário digite um número que já foi digitado anteriormente, o programa deverá pedir para ele digitar outro número. Exibir na tela o vetor final que foi digitado.   

l = []  
while len(l) < 12: 
    n1 = int(input(""))
    if n1 not in l: 
        l.append(n1)    
    else:   
        print(f"Numero {n1} ja existe, escreva outro")  
print(l)