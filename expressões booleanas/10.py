#Faça uma função que receba 2 números inteiros positivos e calcule o Máximo Divisor Comum (MDC).    
def funcao(x1,x2):
    mdc = 1
    y1 = x1
    y2 = x2 
    div = 2
    c = 0 
    while c < x1 and c < x2:
        div = 2
        while div <= y1 or div <= y2:
            if y1%div == 0 and y2%div == 0:
                y1 = y1/div
                y2 = y2/div
                mdc *= div
            div += 1
        c += 1
    return mdc