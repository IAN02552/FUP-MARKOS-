#Faça um programa que conte o número de 1’s que aparecem em uma string. Exemplo: 0011001 -> 3. Não use nenhuma funcionalidade do python que já faça isso.   
pal = str(input(""))
cont = 0
for c in range(len(pal)):
    if pal[c] == "1":
        cont += 1
print(cont)