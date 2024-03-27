#Faça uma função que calcule e retorne a soma dos N primeiros números pares (considere o 0 como o primeiro número par). 
def funcao(x):  
    c = 0
    cont = 0
    soma = 0
    while c < x:
        soma = soma+cont
        cont = cont+2   
        c =  c+1
    return soma 
x = int(input(""))
y = funcao(x)
print(f"{y}")