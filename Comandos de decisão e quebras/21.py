#Faça uma função que receba dois números e retorne qual deles é o maior.    
def funcao(x1,x2):  
    maior = x1  
    if x2 > maior:  
        maior = x2  
    return maior    
x1 = float(input(""))
x2 = float(input(""))
y = funcao(x1, x2)
print(f"{y:.2f}")