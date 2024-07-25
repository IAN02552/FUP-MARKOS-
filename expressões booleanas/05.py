# Dados três valores inteiros, A , B e C, verificar se eles podem ser valores dos lados de um triângulo e, se forem, verificar se é um triângulo escaleno, equilátero ou isósceles, considerando os seguintes conceitos:
# O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
# Chama-se equilátero o triângulo que tem três lados iguais.
# Denomina-se isósceles o triângulo que tem o comprimento de dois lados iguais.
# Recebe o nome de escaleno o triângulo que tem três lados diferentes.  
a = int(input(""))  
b = int(input("")) 
c = int(input(""))  
if a < b+c and b < a+c and c < +a+b:  
    if a == b and c == b:   
        print("Triangulo equilatero")   
    elif a != b and b != c and a != c:  
        print("Triangulo escaleno") 
    else:   
        print("Triangulo isosceles")    
else:   
    print("Nao triangulo")