#Faça um programa que receba uma palavra e um caractere (vogal ou consoante) e imprima quantas vogais (a, e, i, o, u) possui essa palavra. Substitua todas as vogais da palavra dada pelo caractere dado, e imprima a nova palavra. 
pal = str(input(""))    
vc = str(input("")) 
res = ""    
cont = 0   
for c in range(len(pal)):   
    if pal[c] in "aeiouAEIOU":  
        res += vc   
        cont += 1   
    else:   
        res += pal[c]   
print(cont)  
print(res)