# Digite um nome e imprima quantas letras diferentes tem um nome. 
    
nome = str(input(""))   
l = [nome]  
controle = []   
quant = 0   
for c in range(len(l[0])): 
    if l[0][c] not in controle and l[0][c] != " " and l[0][c] != "-":  
        controle.append(l[0][c])   
        quant += 1  
    
print(quant)