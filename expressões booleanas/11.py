#Faça uma função que receba uma cadeia de caracteres no formato “DD/MM/AAAA” e retorne o dia, mês e ano para 3 variáveis inteiras. Nessa função, verifique se as barras estão no lugar certo, e se DD, MM e AAAA são numéricos. Caso alguma verificação não seja válida, os retornos devem ser iguais a zero.   
def funcao(x):
    y1 = x[0]+x[1]
    y2 = x[3]+x[4]
    y3 = x[6]+x[7]+x[8]+x[9]
    res = y1+y2+y3
    if "/" in res or "a" in res:
        return 0,0,0
    else:
        return int(y1),int(y2),int(y3)