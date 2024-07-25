# Implemente a função h definida recursivamente por: h(m, n) = m + 1, se n = 1; h(m, n) = n + 1, se m = 1, h(m, n) = h(m, n − 1) + h(m − 1, n), se m > 1, n > 1.    
def h(m,n): 
    if n == 1:
        return m+1
    elif m == 1:
        return n+1
    else:
        return h(m,n-1)+h(m-1,n)