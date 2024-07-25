# Faça uma função que receba um vetor e um número inteiro x e retorne os múltiplos do número x que existem no vetor.    

def funcao(x1,x2):  
    controle = []   
    for c in range(len(x1)):    
        if x1[c]%x2 == 0:   
            controle.append(x1[c])  
    return controle 

x1 = []
for i in range(10):
    x1.append(int(input("")))
x2 = int(input(""))
y = funcao(x1, x2)
print(y)