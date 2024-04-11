#Escreva uma função que gera um triângulo lateral de altura 2 × n − 1 e n de largura. Por exemplo, a saída para n = 4 seria:
# *
# **
# ***
# ****
# ***
# **
# * 
def funcao(x):  
    for i in range(x):
        for c in range(i+1):
            print("*",end = " ")    
        print() 
    for i in range(x-1):
        for c in range(x-1-i):
            print("*",end = " ")    
        print()    
x = int(input(""))
funcao(x)  