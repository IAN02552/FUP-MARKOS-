#Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou por 5, mas não simultaneamente pelos dois.   
n1 = int(input("")) 
if n1%3 == 0 and n1%5 == 0: 
    print("False")  
elif n1%3 == 0 or n1%5 == 0:    
    print("True")   
else:   
    print("False")