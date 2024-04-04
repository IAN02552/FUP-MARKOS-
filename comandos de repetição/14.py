#Em Matemática, o número harmônico designado por H(n) define-se como sendo a soma da série harmônica: H(n) = 1/1 + 1/2 + 1/3 … 1/n. Faça uma função que, dado um valor n inteiro positivo, calcule o valor de H(n). 
def funcao(x):
    hn = 1
    soma = 0
    for c in range(2,x+1):
        soma = soma+1/c
    hn = hn+soma 
    return hn   
x = int(input(""))
y = funcao(x)
print(f"{y:.2f}")