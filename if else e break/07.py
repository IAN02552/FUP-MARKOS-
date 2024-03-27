#Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário então imprima: "Emprestimo nao concedido", caso contrário imprima: "Emprestimo concedido".   
n1 = float(input(""))   
emp = float(input(""))  
if n1*0.20 >= emp:  
    print("Emprestimo concedido")   
else:   
    print("Emprestimo nao concedido")