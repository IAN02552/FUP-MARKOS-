#Escreva um programa que leia duas palavras e diga qual delas vem primeiro na ordem alfabética. Não use nenhuma funcionalidade do python que já faça isso. Dica: ‘a’ é menor do que ‘b’.    
pal = str(input(""))
pal1 = str(input(""))
maior = 0
controle1 = len(pal)
controle2 = len(pal1)
if len(pal) >= len(pal1):
    maior = len(pal)
else:
    maior = len(pal1)
for c in range(maior):
    if c == maior-1:
        if ord(pal[c]) <  ord(pal1[c]):
            print(pal)
            break
        else:
            print(pal1)
            break

    if ord(pal[c]) <  ord(pal1[c]) or c == controle1-1:
        print(pal)
        break
    if ord(pal1[c]) < ord(pal[c]) or c == controle2-1:
        print(pal1)
        break