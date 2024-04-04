#O número de Fibonacci Fn para n > 0 é definido da seguinte maneira:
#◦ F1 = 1
#◦ F2 = 1
#◦ Fn = Fn−1 + Fn−2 para n> 2
#Faça uma função que receba um valor inteiro n e calcule e Fn.  
def funcao(x):
    p1 = 1
    p2 = 1
    pn = 1 
    for c in range(3,x+1):
        p1 = p2
        p2 = pn
        pn = p1+p2 
    return pn   
x = int(input(""))
y = funcao(x)
print(f"{y}")