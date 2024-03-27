#Escreva um programa que leia a idade e o primeiro nome de várias pessoas. Seu programa deve terminar quando uma idade negativa for digitada. Ao terminar, seu programa deve escrever o nome e a idade das pessoas mais jovens e mais velhas.   
idade = 0 
controle = 0    
nidade = 0  
vidade = 0  
nnome = ""  
vnome = "" 
while True: 
    nome = str(input(""))   
    idade = int(input(""))  
    if idade < 0:   
        break   
    if controle == 0:   
        nidade = vidade = idade 
        nnome = vnome = nome   
        controle += 1  
    if idade < nidade:  
        nidade = idade  
        nnome = nome    
    if idade > vidade:  
        vidade = idade  
        vnome = nome    
print(nnome)
print(nidade)       
print(vnome) 
print(vidade)