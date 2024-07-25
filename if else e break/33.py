# Dado um número n inteiro e positivo, dizemos que n é perfeito se n for igual à soma de seus divisores positivos diferentes de n. Construa um programa que verifica se um dado número é perfeito. Ex: 6 é perfeito, pois 1 + 2 + 3 = 6. 
n1 = int(input("")) 
div = 0 
for c in range(1,n1): 
    if n1%c == 0: 
        div += c    
if div == n1:   
    print("Perfeito")   
else:   
    print("Nao perfeito")   
  