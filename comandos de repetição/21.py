#Escreva uma função que gera um triângulo de altura n e lados 2 × n − 1 . Por exemplo, a saída para n = 6 seria:
#      *
#     ***
#    *****
#   *******
#  *********
# ***********   
def funcao(x):
    for c in range(1,x+1):
        for k in range(x-c):    
            print(" ",end= "")  
         
        for j in range(2*c-1):    
            print("*",end = "")  
        print()
x = int(input(""))
funcao(x)