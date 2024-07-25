#Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.  
n1 = float(input(""))   
if n1 > 0: 
    print(f"{n1**(1/2):.2f}")    
else:   
    print("Numero invalido")