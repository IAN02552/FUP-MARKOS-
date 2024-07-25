# Faça uma função que receba um vetor posições e o compacte, ou seja, elimine as posições com valor zero. Para isso, todos os elementos à frente do valor zero, devem ser movidos uma posição para trás no vetor. No final, retorne o vetor compacto.   

def funcao(x):  
    l = []  
    for c in range(len(x)): 
        if x[c] != 0:   
            l.append(x[c])  
    return l

x = []
for i in range(10):
    x.append(int(input("")))
y = funcao(x)
print(y)