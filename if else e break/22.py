#Elabore uma função que receba três notas de um aluno como parâmetros e uma letra. Se a letra for A, a função deverá calcular a média aritmética das notas do aluno; se for P, deverá calcular a média ponderada, com os pesos 5, 3, 2. 
def funcao(x1,x2,x3,x4):
    media = 0
    if x4 == "A":
        media = (x1+x2+x3)/3
    if x4 == "P":
        media = (x1*5+x2*3+x3*2)/10
    return media    
x1 = float(input(""))
x2 = float(input(""))
x3 = float(input(""))
x4 = input("")
y = funcao(x1, x2, x3, x4)
print(f"{y:.2f}")