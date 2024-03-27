#O código de César é uma das mais simples e conhecidas técnicas de criptografia. É um tipo de substituição na qual cada letra do texto é substituída por outra, que se apresenta no alfabeto abaixo dela um número fixo de vezes. Por exemplo, com uma troca de três posições, ‘A’ seria substituído por ‘D’, ‘B’ se tornaria ‘E’, e assim por diante. Implemente uma função que faça uso desse Código de César, entre com uma string e a quantidade de posições e retorne a string codificada. Exemplo:
"""String: A LIGEIRA RAPOSA MARROM SALTOU SOBRE O CACHORRO CANSADO
Nova string com 3 posições: D OLJHLUD UDSRVD PDUURP VDOWRX VREUH R FDFKRUUR FDQVDGR
Observação: caso a letra codificada passe da letra Z, ela deve voltar para o início do alfabeto.""" 
def funcao(x1,x2):
    novapal = ""
    for c in range(len(x1)):
        if ord(x1[c])+x2 > 90 and x1[c] != " ":
            novapal += chr((ord(x1[c])+x2)-26)
        elif ord(x1[c])+x2 <=  90 and x1[c] != " ":
            novapal += chr(ord(x1[c])+x2)
        else:
            novapal += " "
    return novapal  
x1 = input("")
x2 = int(input(""))
y = funcao(x1, x2)
print(f"{y}")