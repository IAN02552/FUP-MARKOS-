#Faça uma função que receba o salário de um funcionário e calcule o valor do novo salário, sabendo que ele recebeu um aumento de 21,37 %.   
def funcao(x):
    salario = x+(x*0.2137)
    return salario  
x = float(input(""))
y = funcao(x)
print(f"{y:.2f}")