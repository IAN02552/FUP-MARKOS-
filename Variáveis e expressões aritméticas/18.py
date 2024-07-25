 #Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.   
n1 = int(input(''))
nota100 = n1//100
n1 = n1%100
nota50 = n1//50
n1 = n1%50
nota20 = n1//20
n1= n1%20
nota10 = n1//10
n1= n1%10
nota5 = n1//5
n1 = n1%5
nota2 = n1//2
n1 = n1%2
nota1 = n1//1
print(nota100)
print(nota50)
print(nota20)
print(nota10)
print(nota5)
print(nota2)
print(nota1)