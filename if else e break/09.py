#Ler três valores e imprimi-los na tela em ordem crescente.  
    
n1=int(input())
n2=int(input())
n3=int(input())
if n3<n2:
    t=n2
    n2=n3
    n3=t
if n2<n1:
    t=n1
    n1=n2
    n2=t
if n2>n3:
    t=n2
    n2=n3
    n3=t
print(n1)
print(n2)
print(n3)
    