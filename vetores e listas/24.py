# Faça uma função que receba dois vetores. Retorne um vetor que seja a intersecção entre os 2 vetores anteriores, ou seja, que contém apenas os números que estão em ambos os vetores. Esse vetor de retorno não deve conter números repetidos. 
    
def funcao(x1,x2):  
    l = []  
    for c in range(len(x1)):    
        if x1[c] in x2 and x1[c] not in l:  
            l.append(x1[c]) 
    return l    
    
x1 = []
for i in range(5):
    x1.append(int(input("")))
x2 = []
for i in range(5):
    x2.append(int(input("")))
y = funcao(x1, x2)
print(y)