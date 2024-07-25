# Faça uma função que receba um vetor com as notas de vários alunos, e retorne a média geral, o desvio padrão (populacional), e quantos alunos estão com nota menor que 7.0.    
    
def funcao(x):  
    media = soma = quant = 0    
    for c in range(len(x)): 
        media += x[c]   
    media /= 15  
    for c in range(len(x)): 
        if x[c] < 7:    
            quant += 1 
        x[c] = x[c]-media
        x[c] = x[c]**2  
        soma += x[c]    
    soma /= 15  
    soma = soma**(1/2)   
    return media,soma,quant

x = []
for i in range(15):
    x.append(float(input("")))
y1, y2, y3 = funcao(x)
print(f"{y1:.2f}")
print(f"{y2:.2f}")
print(f"{y3}")