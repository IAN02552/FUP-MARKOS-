#Ler três valores e imprimi-los na tela em ordem crescente.  
a = int(input(""))  
b = int(input(""))  
c = int(input(""))  
maior = a   
meio = 0
if b >= a and b >= c: 
    maior = b   
if c >= a and c >= b: 
    maior = c   
menor = a   
if b <= a and b <= c: 
    menor = b   
if c <= a and c <= b: 
    menor = c   
if a != b and b != c and a != c:   
    meio = (a+b+c)-menor-maior  
if a == b or c == a or b == c:  
    if a == b:  
        meio = a
    elif b == c:    
        meio = b    
    elif c == a:    
        meio = c
    
print(menor)    
print(meio)    
print(maior)   