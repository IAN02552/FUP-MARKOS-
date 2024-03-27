#Implemente um programa que leia duas strings, str1 e str2, e um valor inteiro positivo N. Concatene N vezes a string str2 ao final da string str1. 
str1 = str(input(""))
str2 = str(input(""))
n1 = int(input(""))
print(str1,end = "")
for c in range(n1):
    print(str2,end = "")