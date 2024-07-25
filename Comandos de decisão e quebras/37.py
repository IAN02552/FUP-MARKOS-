#Faça uma função chamada de simplificada que receba como parâmetro o numerador e o denominador de uma fração. Esta função deve simplificar a fração recebida dividindo o numerador e denominador pelo maior fator possível. Por exemplo, a fração 36/60 simplificada para 3/5 dividindo o numerador e denominador por 12.   

def simplificar(x1,x2):
    maior = 0
    p = 0
    while True:
        p = 0
        maior = int(x1)
        if x2 > x1: 
            maior = int(x2)  
        for c in range(2,maior+1):
            if x1%c == 0:
                if x2%c == 0:   
                    x1 = x1/c   
                    x2 = x2/c
                    p = c
        if p == 0:
            break
    return int(x1),int(x2)
                 
x1 = int(input(""))
x2 = int(input(""))
y1, y2 = simplificar(x1, x2)
print(f"{y1}")
print(f"{y2}")