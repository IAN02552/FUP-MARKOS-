# Faça uma função que, dado um vetor de números reais, ordene os elementos desse vetor do maior para o menor, e retorne o vetor ordenado. Não use nenhuma função de ordenação do python.    

def funcao(x):  
    l = []  
    controle = 0  
    for c in range(len(x)): 
        maior = float("-inf")    
        for j in range(len(x)):   
            if x[j] > maior:    
                maior = x[j]    
                controle = j
        x[controle] = float('-inf')   
        l.append(maior) 
    
    return l


x = []
for i in range(10):
    x.append(int(input("")))
y = funcao(x)
print(y)