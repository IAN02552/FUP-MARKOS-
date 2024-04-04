#O Triângulo de Pascal é um triângulo numérico infinito formado por números binomiais Cn,k, onde n representa o número da linha (posição horizontal) e k representa o número da coluna (posição vertical), iniciando a contagem a partir do zero. O triângulo foi descoberto pelo matemático chinês Yang Hui e, 500 anos depois, várias de suas propriedades foram estudadas pelo francês Blaise Pascal. Escreva um programa que leia um número inteiro n ≥ 0 representando a quantidade de linhas e em seguida mostre o Triângulo de Pascal com as n linhas.
#Exemplo n = 7.
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1  
def fat(x):
    f = 1
    for c in range(1,x+1):
        f *= c
    return(f)
n = int(input(""))
for n in range(n):
    for j in range(n+1):
        cobin = fat(n)/(fat(j)*fat(n-j))
        print(int(cobin),end = " ")
    print()