#Faça um programa que, dada uma string, diga se ela é um palíndromo ou não. Lembrando que um palíndromo é uma palavra que tenha a propriedade de poder ser lida tanto da direita para a esquerda como da esquerda para a direita. Exemplos:
# ovo
# arara
# Socorram-me, subi no onibus em Marrocos.
# Anotaram a data da maratona    
    
pal1 = str(input("")).upper()
pal = ""

# Remover caracteres indesejados
for c in range(len(pal1)):
    char = pal1[c]
    if char != " ":
        if char != ".":
            if char != "-":
                if char != ",":
                    pal += char

cont = -1
r = 0

# Verificar se a palavra é um palíndromo
for c in range(len(pal)):
    if pal[c] == pal[cont]:
        r += 1
    cont -= 1

# Comparar se o número de correspondências é igual ao comprimento da string processada
if r == len(pal):
    print("True")
else:
    print("False")