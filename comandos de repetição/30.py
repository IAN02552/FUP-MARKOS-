#Faça um programa que receba uma palavra e a imprima de trás-para-frente.
palavra = str(input(""))
p = -1
for c in range(len(palavra)):
    print(palavra[p],end = "")
    p = p-1