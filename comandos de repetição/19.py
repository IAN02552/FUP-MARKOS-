#Crie uma função que receba como parâmetro um valor inteiro e gere como saída n linhas como pontos de exclamação, conforme o exemplo abaixo (para n = 5).
# !
# !!
# !!!
# !!!!
# !!!!!  
def funcao(x):
    for c in range(x):
        for j in range(c+1):
            print("!",end = "")
        print() 
x = int(input(""))
funcao(x)