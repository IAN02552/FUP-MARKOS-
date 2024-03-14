#Faça uma função que receba um número inteiro positivo de três dígitos (de 100 a 999). Retorne outro número formado pelos dígitos invertidos do número lido. Exemplo: Entrada = 123, Saída = 321.   
def funcao(x):
    y1 = x%10
    y2 = (x//10)%10
    y3 = x//100
    y4 = y1*100+y2*10+y3
    return y4   
x = int(input(""))
y = funcao(x)
print(f"{y:0}")