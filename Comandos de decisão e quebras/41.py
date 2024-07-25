#Escreva um programa que substitui as ocorrências de um caractere 0 em uma string pelo caractere 1. Não use nenhuma funcionalidade do python que já faça isso.  
pal = str(input(""))
res = ""
for c in pal:
    if c == "0":
        res += "1"
    else:
        res += c
print(res)