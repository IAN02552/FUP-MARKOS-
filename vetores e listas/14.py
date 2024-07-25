# Faça um programa que preencha um vetor com 12 números reais aleatórios (uniformemente distribuídos no intervalo [-10, 10]), mostre esses números, e calcule a quantidade de números negativos e a soma dos números positivos desse vetor. A entrada para o programa é a semente dos números aleatórios.   

  
import random
l = []
n1 = int(input())
random.seed(n1)
quant = 0
soma = 0  
for c in range(12): 
    l.append(random.uniform(-10,10))   

for c in range(len(l)): 
    if l[c] < 0:    
        quant += 1  
    if l[c] > 0:   
        soma += l[c]    
print(quant)
print(f"{soma:.2f}") 