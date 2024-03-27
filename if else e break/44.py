#Faça um programa que receba uma frase e imprima-a de maneira invertida, trocando as letras A (maiúsculas ou minúsculas) por *. Não use nenhuma funcionalidade do python que já faça isso.  
pal = str(input(""))
res = ""
for c in pal:
    if c == "a" or c == "A":
        res += "*"
    else:
        res += c
print(res[::-1])