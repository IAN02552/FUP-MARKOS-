#Crie um programa que diga se duas strings são iguais ou não, analisando caractere a caractere. 
def funcao(x1,x2):
    cont = 0
    if len(x1) == len(x2):
        for c in range(len(x1)):
            if x1[c] == x2[c]:
                cont += 1
    if cont == len(x1):
        return "True"
    else:
        return "False"  
x1 = input("")
x2 = input("")
y = funcao(x1, x2)
print(f"{y}")