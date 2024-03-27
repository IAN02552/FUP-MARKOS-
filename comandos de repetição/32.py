#Faça um programa que leia uma palavra e some 1 no valor ASCII de cada caractere da palavra. Imprima a string resultante.   
str1 = str(input(""))
for c in range(len(str1)):
    letra = ord(str1[c])+1
    print(chr(letra),end = "")