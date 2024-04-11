#Faça uma função que receba como parâmetro o ângulo x (em radianos) e um valor inteiro positivo n . Calcule o valor do seno desse ângulo usando a respectiva série de Taylor: sin(x) = x – x3/3! + x5/5! - … + (-1)n (x2n+1)/(2n+1)!.   
    
def funcao(x, n):
    seno = 0
    termo = x
    fatorial = 1
    for i in range(1, 2 * n + 2, 2):
        seno += termo / fatorial
        termo *= -x * x
        fatorial *= (i + 1) * (i + 2)
    return seno 
x1 = float(input(""))
x2 = int(input(""))
y = funcao(x1, x2)
print(f"{y:.8f}")