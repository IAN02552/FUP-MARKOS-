#Faça um programa que leia 3 notas, verifique se as notas são válidas e exiba na tela a média destas notas com duas casas decimais. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.00 e 10.00, onde caso a nota não possua valor válido, este fato deve ser informado ao usuário e o programa termina.    
media = 0   
controle = 0  
for c in range(3):  
    n1 = float(input(""))   
    if n1 >= 0 and n1 <= 10:    
        media = media+n1    
    else:   
        controle = 1   
        print("Nota invalida")  
        break   
if controle == 0: 
    print(f"{media/3:.2f}")