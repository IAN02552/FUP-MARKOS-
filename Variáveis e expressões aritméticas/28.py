#Construa um programa que leia duas strings fornecidas pelo usuário e verifique se a segunda string lida está contida no final da primeira, retornando o resultado da verificação. 
n1 = str(input(""))
n2 = str(input(""))
i = len(n2)
i = i*-1
print(n2 in n1[i::])