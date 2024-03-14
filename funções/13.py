#Faça uma função que receba um valor em R$ que será dividido entre três ganhadores de um concurso. Sendo que da quantia total:
# O primeiro ganhador receberá 46%;
# O segundo ganhador receberá 32%;
# O terceiro receberá o restante;
# Calcule e retorne a quantia ganha por cada um dos ganhadores. 
def funcao(x):
    y1 = x*0.46
    y2 = x*0.32
    y3 = x*0.22
    return y1,y2,y3 
x = float(input(""))
y1,y2,y3 = funcao(x)
print(f"{y1:.2f}")
print(f"{y2:.2f}")
print(f"{y3:.2f}")