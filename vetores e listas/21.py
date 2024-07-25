# Faça um vetor de tamanho 70 preenchido com o seguinte valor: (i + 5*i) % (i + 1) , sendo i a posição do elemento no vetor. Em seguida imprima o vetor na tela.    

l = []  
for c in range(70): 
    l.append((c+5*c)%(c+1))
print(l)