# Faça uma função recursiva que receba um número inteiro positivo n e retorne o superfatorial desse número. Exemplo de superfatorial: sf (4) = 1! * 2! * 3! * 4! = 288. 
def sf(n):
    if n == 1 or n == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i

        return fatorial * sf(n - 1)
