#Faça um programa que receba um valor em R$ que será dividido entre três ganhadores de um concurso. Sendo que da quantia total:
#O primeiro ganhador receberá 46%;
#O segundo ganhador receberá 32%;
#O terceiro receberá o restante;
#Calcule e imprima a quantia ganha por cada um dos ganhadores
n1 = float(input(''))
n2 = n1*0.46
n3 = n1*0.32
n4 = n1*0.22
print(f"{n2:.2f}")
print(f"{n3:.2f}")
print(f"{n4:.2f}")