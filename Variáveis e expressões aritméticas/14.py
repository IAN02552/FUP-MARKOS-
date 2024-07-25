#leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.
n1 = int(input(''))
n2 = n1%10
n3 = (n1//10)%10
n4 = (n1//100)%10
n5 = n1//1000
print(n5)
print(n4)
print(n3)
print(n2)