n1 = int(input("")) 
n2 = int(input("")) 
maior = menor = 0   
div = 0  
if n1 >= n2: 
    maior = n1  
    menor = n2
if n2 > n1: 
    maior = n2  
    menor = n1
while maior-menor >= 0:    
    maior = maior-menor 
    div += 1    
print(div)   


