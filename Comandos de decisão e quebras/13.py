#Calcule as raízes da equação do 2o grau. Lembrando que: x = (−b± √∆)/(2a), onde ∆ = b2 − 4ac, e  ax2 + bx + c = 0 representa uma equação do 2o grau. A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem "Nao eh equacao do 2o grau".
# Se ∆ < 0 , não existe raiz real. Imprima a mensagem “Nao existe raiz real”.
# Se ∆ = 0 , existe uma raiz real. Imprima a raiz e a mensagem "Raiz unica".
# Se ∆ > 0 , Imprima as duas raízes reais.  
# ax**2+bx+c = 0  
a = float(input(""))    
b = float(input(""))    
c = float(input(""))    
delta = (b**2 - 4*a*c)   
if a == 0:  
    print("Nao eh equacao do 2o grau")      
elif delta == 0:  
    x1 = (-b+delta**(1/2))/(2*a)   
    print(f"{x1:.2f}")   
    print("Raiz unica") 
elif delta > 0:   
    x1 = (-b+delta**(1/2))/(2*a)   
    x2 = (-b-delta**(1/2))/(2*a)   
    print(f"{x1:.2f}")   
    print(f"{x2:.2f}")  
elif delta < 0:   
    print("Nao existe raiz real")      

   
