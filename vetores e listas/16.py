# Faça uma função que receba um vetor e retorne um outro vetor, contendo apenas os elementos que não aparecem repetidos.    

def funcao(x):  
    controle = []   
    for c in range(len(x)): 
        cont = 0
        for j in range(len(x)):   
            if x[j] == x[c]:    
                cont += 1   
        if cont == 1:   
            controle.append(x[c])   
    return controle   

x = []
for i in range(10):
    x.append(int(input("")))
y = funcao(x)
print(y)