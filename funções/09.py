#Crie uma função que, dada uma velocidade em km/h (quilômetros por hora) e retorne-a convertida em m/s (metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em km/h e M em m/s.  
def funcao(x):
    ms = x/3.6
    return ms   
x = float(input(""))
y = funcao(x)
print(f"{y:.2f}")