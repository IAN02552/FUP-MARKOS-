#Faça um função que receba a data atual (cadeia de caracteres no formato “DD/MM/AAAA”) e retorne uma string com a data onde o mês está no formato textual por extenso. Considere que a data é válida. Exemplo: Data: 01/01/2000, retornar: 1 de janeiro de 2000.    
def funcao(x):
    meio = ""
    controle = ""
    res = ""
    for c in range(len(x)):
        if c == 3 or c == 4:
            controle += x[c]
    if controle == "01":
        meio += " de janeiro de "
    if controle == "02":
        meio += " de fevereiro de "
    if controle == "03":
        meio += " de marco de "
    if controle == "04":
        meio += " de abril de "
    if controle == "05":
        meio += " de maio de "
    if controle == "06":
        meio += " de junho de "
    if controle == "07":
        meio += " de julho de "
    if controle == "08":
        meio += " de agosto de "
    if controle == "09":
        meio += " de setembro de "
    if controle == "10":
        meio += " de outubro de "
    if controle == "11":
        meio += " de novembro de "
    if controle == "12":
        meio += " de dezembro de "
    incio = ""
    fim = ""
    if x[0] == "0":
        incio += x[1]
    if x[0] != "0":
        incio += x[0]
        incio += x[1]
    for c in range(4):
        fim += x[c+6]
    res += incio
    res += meio
    res += fim
    return res  
x = input("")
y = funcao(x)
print(f"{y}") 