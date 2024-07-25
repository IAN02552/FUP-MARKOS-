#Faça um programa que receba do usuário uma string. O programa imprime a string sem suas vogais.  
pal = str(input(""))
res = ""
for c in range(len(pal)):
    if pal[c] in "aeiou" or pal[c] in "AEIOU":
        res += ""
    else:
        res += pal[c]   
print(res)