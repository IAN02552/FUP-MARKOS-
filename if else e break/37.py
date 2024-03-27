#Faça uma função chamada de simplificada que receba como parâmetro o numerador e o denominador de uma fração. Esta função deve simplificar a fração recebida dividindo o numerador e denominador pelo maior fator possível. Por exemplo, a fração 36/60 simplificada para 3/5 dividindo o numerador e denominador por 12.   
def simplificar(x1,x2):
    c = 0
    y1 = x1
    y2 = x2
    while c < x1 or c < x2:
        p = 2 
        while p <= y1 or p <= y2:
            if y1%p == 0 and y2%p == 0:
                y1 = y1/p
                y2 = y2/p
            p += 1
    
        c += 1
    return int(y1),int(y2)  
x1 = int(input(""))
x2 = int(input(""))
y1, y2 = simplificar(x1, x2)
print(f"{y1}")
print(f"{y2}")