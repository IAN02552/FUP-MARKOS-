# Faça uma função que receba dois vetores de mesmo tamanho e calcule outro vetor contendo, nas posições pares o valores do primeiro vetor e nas posições ímpares os valores do segundo vetor.   

def funcao(x1,x2):  
    tam = len(x1)  
    C = [None]*(tam*2)  
  
    for c in range(tam): 
        C[c*2] = x1[c]  
        C[c*2+1] = x2[c]    
    return C

    


x1 = []
for i in range(5):
    x1.append(int(input("")))
x2 = []
for i in range(5):
    x2.append(int(input("")))
y = funcao(x1, x2)
print(y)