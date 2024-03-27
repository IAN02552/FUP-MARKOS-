#Ler uma frase e contar quantos caracteres são brancos. Não use nenhuma funcionalidade do python que já faça isso.  
pal = str(input(""))
cont = 0
for c in range(len(pal)):
    if pal[c] == " ":
        cont += 1
print(cont)