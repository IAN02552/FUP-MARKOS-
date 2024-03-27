#O numero 3025 possui uma característica interessante, sendo a seguinte: 30 + 25 = 55 e     55**2 = 3025. Elaborar um algoritmo que verifique todos os números de quatro algarismos que apresentem essa propriedade. Não use operações com strings.   
n1 = n2 = 0    
for c in range(1000,9999):  
    n1 = c//100 
    n2 = c%100  
    if (n1+n2)**2 == c: 
        print(c)