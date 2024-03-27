#Faça um programa que, dada uma string, diga se ela é um palíndromo ou não. Lembrando que um palíndromo é uma palavra que tenha a propriedade de poder ser lida tanto da direita para a esquerda como da esquerda para a direita. Exemplos:
# ovo
# arara
# Socorram-me, subi no onibus em Marrocos.
# Anotaram a data da maratona   
pal1 = str(input("")).upper()
pal = ""
for c in range(len(pal1)):
    if pal1[c] != " " and pal1[c] != "." and pal1[c] != "-" and pal1[c] != ",":
        pal += pal1[c]
cont = -1
r = 0
for c in range(len(pal)):
    if pal[c] == pal[cont] and pal[c] != " ":
        r += 1
    cont = cont-1
if r == len(pal):
    print("True")
else:
    print("False")